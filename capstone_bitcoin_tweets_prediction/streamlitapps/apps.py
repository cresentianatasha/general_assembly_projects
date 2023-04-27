import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit
from datetime import datetime
import datetime as dt
import yfinance as yfin
import pandas_datareader.data as pdr
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score   
 
df = pd.read_csv('../data/8-lag-feature-day.csv')
text = pd.read_csv('../data/3-preprocessed_tweets.csv')

#loading the model
with open("Model/trained_model_dir_lr.sav", "rb") as to_read:
    model_dir = pickle.load(to_read)
with open("Model/trained_model_mag_rf.sav", "rb") as to_read:
    model_mag = pickle.load(to_read)

def period_selection (df,input_start_date,input_end_date):
    df = df[(df['timestamp'] >= input_start_date) & (df['timestamp'] <= input_end_date)]
    df.set_index('timestamp',inplace=True)
    return df

#from yahoo finance
yfin.pdr_override()
def btc_data(start,end):
    crypto = 'BTC'
    against_currency = 'USD'

    #start = dt.datetime(2016,1,1)
    #end = dt.datetime(2018,12,31)

    df = pdr.get_data_yahoo("BTC-USD", start=start, end=end)
    df = df.groupby(df.index.date, group_keys=False).apply(vwap)
    df = df[['Close','VWAP']]   
    return df

def vwap(df):
    q = df['Volume']
    p = (df['High'] + df['Low'] + df['Close']) / 3
    return df.assign(VWAP=(p * q).cumsum() / q.cumsum())    

# def plot_words(tw_df,vectorizer,start,end):
#     df_ = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
#     vectorizer_dict = {'CountVectorizer':CountVectorizer(),'TFIDF': TfidfVectorizer()}
#     model = vectorizer_dict[vectorizer]
#     model.fit(tw_df['text'])
#     col_vec = model.transform(tw_df['text'])
#     col_df = pd.DataFrame(col_vec.todense(),columns=model.get_feature_names_out())
#     col_df.sum().sort_values(ascending=False).head(10).plot(kind='barh');
#     plt.title('Top 10 Words in Tweets')
#     return col_df

def choose_data(df,to_choose):
    if to_choose == 'direction':
        structure_direction = [
        'pos_pol (t-1)','neg_pol (t-1)', 'Close (t-1)', 'text (t-1)','VWAP (t-1)','direction (t-1)',
        'pos_pol (t-2)','neg_pol (t-1)', 'Close (t-2)', 'text (t-2)','VWAP (t-2)','direction (t-2)',
        'pos_pol (t-3)','neg_pol (t-1)', 'Close (t-3)', 'text (t-3)','VWAP (t-3)','direction (t-3)'
    ]
        return df[structure_direction],df['direction']
    elif to_choose == 'magnitude':
        structure_magnitude = [
            'pos_pol (t-1)','neg_pol (t-1)', 'Close (t-1)', 'text (t-1)','VWAP (t-1)','binned (t-1)',
            'pos_pol (t-2)','neg_pol (t-1)', 'Close (t-2)', 'text (t-2)','VWAP (t-2)','binned (t-2)',
            'pos_pol (t-3)','neg_pol (t-1)', 'Close (t-3)', 'text (t-3)','VWAP (t-3)','binned (t-3)',
        ]
        return df[structure_magnitude],df['binned']
    
def predict_btc(x_dir,y_dir,x_mag,y_mag,df):
    dir_x,dir_y = choose_data(df,'direction')
    mag_x,mag_y = choose_data(df,'magnitude')

    dir_pred = model_dir.predict(dir_x)
    mag_pred = model_mag.predict(mag_x)
    dir_acc = accuracy_score(dir_y,dir_pred)
    mag_acc = accuracy_score(mag_y,mag_pred)
    return dir_pred,mag_pred,dir_acc,mag_acc


def decision(x,y,y1,y2):
    if (x == 1) and (y >= y2):
        return 1
    elif (x == 0) and (y <= y1):
        return -1
    #elif (x == 0) and (y == 1):
        #return -1
    else:
        return 0

def final_compiler(df,start,end,threshold,initial_money,y1,y2,buy_dollar_fraction,sell_btc_fraction):
    df_ = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
    df_.set_index('timestamp',inplace=True)
    x_dir,y_dir = choose_data(df_,'direction')
    x_mag,y_mag = choose_data(df_,'magnitude')
    dir_pred,mag_pred,dir_acc,mag_acc = predict_btc(x_dir,y_dir,x_mag,y_mag,df_)

    #new df for finalization
    final_df = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
    final_df['prediction_dir']=dir_pred
    final_df['prediction_mag']=mag_pred.astype(int)
    final_df['decision'] = final_df.apply(lambda row: decision(row['prediction_dir'], row['prediction_mag'],y1=y1,y2=y2),axis=1) #to take the rows

    #predicting monetary value
    buy_time,sell_time = [],[]
    btc= 0
    initial = initial_money
    for i,row in final_df.iterrows():
        if btc == 0:
            if row['decision'] == 1:
                btc += (initial/row['Close'])
                initial -= initial
                buy_time.append(row['timestamp'])
        elif (btc!=0) and (initial>=0):
            if (row['decision'] == 1) and (initial>threshold):
                btc += (buy_dollar_fraction/row['Close'])
                initial -= buy_dollar_fraction
                buy_time.append(row['timestamp'])
            elif (row['decision'] == -1):
                btc -= (btc*sell_btc_fraction)
                initial +=((btc*sell_btc_fraction)*row['Close'])
                sell_time.append(row['timestamp'])
        elif initial<0:
            print ("You blew up your account",sell_time[-1])
            break
    initial +=( btc*final_df['Close'].tolist()[-1])

    return (initial,buy_time,sell_time)