# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Singapore Dengue Prediction Through Google Trend and Weather Data

Government has allocated budget for each department every year. As part of NEA data science team, we would like to ensure that we have solid measure for dengue prevention starting from Project Wolbachia, fogging to . Due to limited budget, **our team has been tasked to proposed effective fogging plan.**

In this project, as part of Data Science team in NEA, **we will be forecasting dengue case by using machine learning** on Singapore weather data and Google Trend (based on certain google search keywords) with dengue case data from Jul'2015 to Dec'2019. 

**SUCCESS METRICS** our goal is to have a model to be able to predict the denge case number as close as possible, therefore, we will be choosing the *Root Mean Squared Error (RMSE)* as we will be approaching this problem as a regression problem. RMSE itself measured the difference between the predicted values and actual values, **the smaller it is, the better our model performs**

**CONCLUSION** our model from linear regression, XGBoost, LSTM even to time series SARIMA model is *unable to give a perfect prediction* due to the lack of relevant features. 

However, we would like to give more attention to the spatial analysis and dengue case distribution. We suggest that **NEA allocated more fogging sessions on these 5 locations**(4 in the east and 1 in the northwest) then followed by Jurong West, Choa Chu Kang and then Newton subsequently.

Aside from the location, we suggest on the timing as well. Looking at the past 5 years data, there is a tendency for the case to go up and peak around July.

This shows how we can put our resources efficiently by **putting more fogging sessions on June (due to 2 weeks incubation, mosquitoes might breed during this timing) to October**.

## Notebook Navigation--------------------------------------------------------------------------------
1. Data Scraping
2. Dataset Overview, Data Preprocessing, and EDA
    - Background
    - Problem Statement and Success Metrics
    - Dataset First Look
    - Data Preprocessing
    - Final Dataset Overview
        - Features Correlation
        - Spatial Analysis using K-Means Clustering
        - Dengue Case Distribution Throughout the Months
3. Modeling
    - Baseline Model
    - Linear Regression (Non square rooted and square rooted features)
    - XGBoost (Non square rooted and square rooted features)
    - Long Short Term Memory/ LSTM
    - Vector Auto Regression
    - ARIMA 
    - SARIMA 
4. Model Summary
5. Recommendation
    - Adding the monthly number of tourist from Southeast Asia
    - Adding the monthly Rainy Day, Hourly Sunshine, Minimum Humidity Percentage, and Relative Humidity Percentage (24hours)
## ----------------------------------------------------------------------------------------------------

*tl;dr*
- 8 Centroids observed from elbow method deduction in K-Means Square as part of spatial analysis:
    How is it deducted? Weighted K-Means clustering based on total number of case in the cluster.
    Eastern part of Singapore is highly populated and urbanised, therefore, dengue fever outbreak has high prevalence in the east. 

    ||Latitude|Longitude|Address|
    |---|---|---|---|
    |Centroids 1|1.357561|103.946310| **[Top5]** 70 Tampines Avenue 4, Singapore, 529681|
    |Centroids 2|1.379080|103.868603| **[Top5]** 5006 Ang Mo Kio Avenue 5, Singapore, 569873|
    |Centroids 3|1.306131|103.838893| [8] 8 Cairnhill Circle, Singapore, 229814 (Newton)|
    |Centroids 4|1.341684|103.709469| [6] 25 Boon Lay Drive, Singapore, 649922 (Jurong West)|
    |Centroids 5|1.437334|103.809485| **[Top5]** Woodlands Avenue 12, Singapore|
    |Centroids 6|1.352729|103.865674| **[Top5]** 250 Lorong Chuan, Singapore, 556748 (Serangoon)|
    |Centroids 7|1.318858|103.899753| **[Top5]** 410 Eunos Road 5, Singapore, 400410|
    |Centroids 8|1.378721|103.745003| [7] 251A Choa Chu Kang Avenue 2, Singapore, 681251|

- Modeling Summary
    |**Model**|**RMSE**|**Remarks**|
    |---|---|---|
    |Baseline|157.35|Using the mean to predict the dengue case number|
    |Linear Regression|25.03| Improvement from baseline but R2 score is <1%, minmaxscaler is used as the range of these features is well defined (temp, rainfall, google trend relative interest score)|
    |Linear Regression with Square Rooted Features|**16.12**|Improvement from previous LR model of R2 score to 57% and another form of normalization by square rooting the features help the model performance, lag1 is the best predictor = our model to predict **the next 1 to 2 weeks dengue case number in Singapore** based on Temp, Rainfall, and Google Trend Data|
    |XGBoost|17.15|Downside that this is a blackbox model and not able to pinpoint the important features|
    |XGBoost with Square Rooted Features|16.08|Downside that this is a blackbox model and not able to pinpoint the important features|
    |LSTM|61.75|Transforming our data to take count of previous study based on 4 week window (predict the 5th week)- unable to perform well|
    |VAR|16.82|using time series model, easily going to mean. Unable to be used for long term prediction|
    |SARIMA|18.102|improvement from VAR model, but our model seems to be quite worst off than a simple linear regression model|

The overall best model is Linear Regression on square rooted features to predict the next 1 to 2 weeks dengue case. The most important features are Highest 120 min rainfall and dengue fever google trend search. **This is an interesting finding on how people leverage google trend search term and that shows how people are more interested in this topic which most of the time is when the case is increasing**

- Exploration to Improve Model Performance 
    We have tried to get more data such as 
    1. Monthly Singapore tourist arrival data from Southeast Asia as those countries tend to have more dengue cases due to the warm weather
    2. Monthly rainy day, hourly sunshine, and humidity percentage 
    However, these data turns out to be a *noise* to our model. 
    
    Therefore, another suggestion to **NEA is to allocate budget to collect weekly data of relevant features** such as humidity percentage, weekly rainy day or even on how old the HDB building is on the dengue confirmed case location because older building might be more porous creating location of stagnant water for mosquito breeding. Another interesting feature will be Singapore population as dengue outbreak tends to spread between affected people through mosquitoes bite.


