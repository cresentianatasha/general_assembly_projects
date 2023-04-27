### design for streamlit apps87tdxz

import pandas as pd
import pickle
import streamlit as st
from PIL import Image
from datetime import datetime
#import the models
from apps import final_compiler,period_selection,btc_data,vwap,choose_data,predict_btc,decision

#loading the model
with open("./Model/trained_model_dir_lr.sav", "rb") as to_read:
    model_dir = pickle.load(to_read)
with open("./Model/trained_model_mag_rf.sav", "rb") as to_read:
    model_mag = pickle.load(to_read)

df = pd.read_csv('../data/8-lag-feature-day.csv')
text = pd.read_csv('../data/3-preprocessed_tweets.csv')

#set the page layout

st.set_page_config(page_title="demo.py",
                   layout="wide"
                   )
#logo and brand name
col1,col2 = st.columns([0.4,0.9])
with col1:
    st.image('tweebit.jpg', width=300)
with col2:
    st.title('_A Proof of Concept: Bitcoin Price Prediction from Twitter Tweets Sentiment Analysis and Volume_')
st.caption("""
Crypto has less regulation on it, trades for 24x7 and provides great price volatility which can be a risk and room for profit.
Many ways to predict bitcoin price: technical analysis, fundamental analysis and sentiment analysis. 
For some retail investor, this means preparing their trading plan, going through news and candlestick bars which probably take almost an hour. 
If we believe that Bitcoin price is indeed moved along with people’s opinion, do we want to waste our time to scroll through those tweets or spend less than a minute to get gist of it?

**Tweebit provides a one stop analysis on Twitter tweets sentiment analysis taken from 9M tweets during period of interest.**
 """)
st.write("---")

#feature introduction
st.sidebar.header('**Features Captured**')
st.sidebar.markdown('**1. Positive Polarity**: Vader generated score related to the tweet positive polarity')
st.sidebar.markdown('**2. Negative Polarity**: Vader generated score related to the tweet negative polarity')
st.sidebar.markdown('**3. Tweet Volume**: calculating the volume of biased tweets based on Vader')
st.sidebar.markdown('**4. VWAP**: Bitcoin Volume Weighted Average Price at end of day')
st.sidebar.markdown("---")

# Create a form for user input
st.header('Input Your Period of Interest')

# Create a date for user input
with st.form("my_form"):
    col3,col4 = st.columns([0.5,0.5])
    with col3:
        start_date = st.date_input('Choose Start Date', value=datetime(2018,12,31),min_value=datetime(2016,1,1),max_value=datetime(2018,12,31),key=1)

    with col4:
        end_date = st.date_input('Choose End Date', value=datetime(2018,12,31),min_value=datetime(2016,1,1),max_value=datetime(2018,12,31),key=2)
        if start_date>end_date:
            st.error('This is an error', icon="🚨")
    st.write("---")

    #understanding trader risk appetite
    st.header("Let's Assess Your Risk Appetite!")
    col5,col6 = st.columns([0.5,0.5])
    with col5:
        initial = st.number_input('Initial Amount of Money', min_value=0,step=100)
    with col6:
        threshold = st.number_input('Threshold: the minimum amount before we stop buying', min_value=0,step=100)
        if (threshold>initial):
            st.error('This is an error', icon="🚨") 
    col7,col8 = st.columns([0.5,0.5])
    with col7:
        y1 = st.slider('How Eager You Like to Sell (1: least risk, 4: higher risk)', min_value=0, max_value=4, step=1)
    with col8:
        y2 = st.slider('How Eager You Like to Buy (1: least conservative, 4: most conservative)', min_value=0, max_value=4, step=1)
    col9,col10 = st.columns([0.5,0.5])
    with col9:
        #sell_btc_fraction = st.slider('How much of a fraction you would like to **sell**', min_value=0.0, max_value=0.9, step=0.1)
        sell_btc_fraction = st.slider(
        label="Percentage of BTC you would like to sell/trade",
        min_value=0,
        max_value=100,
        value=50,
        format="%d%%",
        step = 5,
        )
        st.write(sell_btc_fraction)
    with col10:
        #buy_dollar_fraction = st.slider('How much of a fraction you would like to **buy**', min_value=0, max_value=initial, step=1)   
        buy_dollar_fraction = st.slider(
        label="Percentage of your initial you would like to buy/trade",
        min_value=0,
        max_value=100,
        value=50,
        format="%d%%",
        step = 5,
        )
        st.write(buy_dollar_fraction)
        buy_dollar_fraction = initial * buy_dollar_fraction
    #submit button
    submitted = st.form_submit_button("Submit")

    # When the user submits the form, make a prediction and display the results
    if submitted:
        final_money,buy_time,sell_time = final_compiler(df,start=start_date.strftime("%Y-%m-%d"),end=end_date.strftime("%Y-%m-%d"),threshold=threshold,initial_money=initial,y1=y1,y2=y2,buy_dollar_fraction=buy_dollar_fraction,sell_btc_fraction=sell_btc_fraction)
        
        col11,col12 = st.columns([0.3,0.3])
        with col11:
            st.write(f'Initial Money: ${initial}')
        with col12:
            st.write(f'Money Left: ${final_money}')
        if final_money-initial<0:
            col13,col14 = st.columns([0.3,0.3])
            with col13:
                st.image('loss.jpeg', width=100)
            with col14:
                st.write(f'You lost : ${final_money-initial}')
        else:
            col13,col14 = st.columns([0.3,0.3])
            with col13:
                st.image('gain.png', width=100)
            with col14:
                st.write(f'You gained: ${final_money-initial}')
        st.write(f'You Need to buy: {buy_time}')
        if sell_time != []:
            st.write(f'You Need to sell: {sell_time}')
