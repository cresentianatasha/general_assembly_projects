# Project 2 - Ames Housing Data and Kaggle Challenge

**Primary Learning Objectives:**
1. Creating and iteratively refining a regression model
2. Using [Kaggle](https://www.kaggle.com/) to practice the modeling process
3. Providing business insights through reporting and presentation.

**Background**
Buying a house is seen as a big purchase. Many factors can affect the price, starting from external factor such as economic situation and internal factor such as house features. In this project, we have the housing price data along with the features of each house.

**Problem Statement**
This project is overlooking the housing sale in Ames, Iowa, USA. We will take a look on the house features from houses sold in Ames. These questions are some questions that we would like to find out:
1. What features increase the saleprice?
2. What features reduce the saleprice?

The goal of this project it to **predict the saleprice based on the features given**, which will benefit both homeowners and potential home buyers to make a data-driven estimated price based on the features of the house that they are selling or looking for.

First, we will understand the training set features first and handle missing values. Then, we will be doing feature selection, scaling and train-test-split followed by linear regression models. Performance measurement is using **R2 score** which gives use the percentage of variability that can be explained using this model and **Root Mean Squared Error** to see how well our prediction is.

**Methodology**
We will start by defining our Null Model. Then, we will have four different models to see how we can improve our model:
1. Ordinary Linear Regression Model
2. Ridge Regression Model
3. Lasso Regression Model
4. ElasticNet Regression Model

**Insights**

**In the Linear Regression model with y value log transformed, we can see that the prediction is more linearly correlated, which means the model performed better than the Lasso.** Therefore, it is no surprise that our submission for RMSE value is also lower using this Linear Regression compared to Lasso.

Although Lasso might not perform as well as the Linear Regression Model. We can deduce few things from the lasso coefficient. External material is not a really significant features that influence the saleprice. Therefore, if homeowners would like to increase their house saleprice, rather than spending on a very expensive external material, they can first focus on **renovating the house to improve Overall Quality and General Living Area size.** If these qualities have been satisfied, then we can look at **basement full bathroom, kitchen quality and to add fireplace feature if you don't have any.**

Aside from that, we observe there are certain neighbourhoods that are not really preferred such as Edwards, Old Town, Iowa DOT and Rail Road. These areas have quite old buildings and some of the buildings in Edwards has planned to be repurposed to be City of Ames Park. Therefore, homebuyers can probably **avoid these areas and look for a rather newer or remodelled houses with better overall quality in GreenHill, Stone Brook, Northridge area.**

**Kaggle Submission**
Lasso
Public = 32551.87436
Private = 22981.34329

Linear Regression
Public = 27096.25499
Private = 21755.89945

