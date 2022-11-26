# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: NLP Subreddit Classifications

### Description

As a part of marketing division of an invesment club, we would like to create a list of suggested post/news based on comments left by user in the discussion thread. This enables us to create a curated content that suits our member's interest.

From the beginning of COVID, people shows significant interest on how to frow their money. There are many investement instruments to do so such as stock and crypto currency. Stock represents the share of company ownership where the price is based on market's expectation on future growth for the company, while crypto currency is digital currency which uses cryptography to secure it. 

Crypto has taken the spotlight by multiple stories of overnight billionaires, creating huge interest for people to own them. Crypto has an extreme volatility which means one will be exposed to a higher risk to get higher return compare to stock. These two have distinct difference such as how they are controlled, stock is controlled by the company's performance, but crypto allows decentralized approached without any government control. There are many other differences among them, but while discussing these topics, the words used is quite similar. For example, crypto exchanges use a central limit order book and order matching algorithms just like in stock market.

As market activity will drive the price, people tend to discuss and exchange their analysis before making any trade. Reddit is a popular platform for peole to discuss topics anonymously. A broad topic can be cateforized to a subreddit where people can share their thoughts, ask questions or opinions from others. The huge interest of these topics is reflected by the number of users in each subreddits, r/stocks with 4.9M users and r/CryptoCurrency with 5.8M users.


#### About the API

Pushshift's API is fairly straightforward. For example, if I want the posts from [`/r/boardgames`](https://www.reddit.com/r/boardgames), all I have to do is use the following url: https://api.pushshift.io/reddit/search/submission?subreddit=boardgames

**NOTE:** Pushshift now limits you to 100 posts per request (no longer the 500 in the screencast).


### Problem Statement
Creating a model to do binary text classification (stocks/ CryptoCurrency) based on the post where the model then can be implemented to classify member's discussion thread.

The **goal of our model** is to get a good degree of separation between the two classes. This can be represented by Receiver Operating Characteristics Area Under the Curve **(ROC-AUC)**. ROC curve is a probability curve that shows model performance at all classification threshold with 2 parameters which is True Predicted Positive (TPR) and False Predicted Positive (FPR). The area under the curve represents the degree of separability between classes.

### Methodology

- We will start by scrapping using push shift API from r/stocks and r/CryptoCurrency subreddits followed by removal of the duplicates and other data pre-processing steps so that we can create token from the subreddit post. 
- We will then validate the token's principal components using PCA algorithm to check how well the separatation is. 
- We will continute to fit our features to Supervised Learning Models for binary classifications (logistic regression, k-nearest neighbors, naive bayes, SVC and random forest) and evaluate based on ROC score along with the learning curve to see if there is any potential to improve our model.
- Finally, we will then dive in deeper to our best model to check the optimal threshold

### Conclusion

Final chosen model is **Multinomial Naive Bayes with Count Vectorizer**. Few pointers on our final model:
- Focusing on the vectorizer part, it seems that **pre-trained embedded vectors perform worst across all models**. This is expected from the first principal component analysis whereby there are many points from opposite class in a class region. The potential reason of the low performance might be due to outdated trained data as stocks and crypto are very dynamic, the terminology might not have been captured in both Google Word2Vec and Global Vectors.

- Across all models, we observed using **ngram_range = (1,2) is found to be beneficial** to increase our accuracy score. This is because of our vectorizer past both unigram ("apple" and "stock") and bigrams ("apple stock").

- Baseline model chosen was based on threshold at 0.5 with ROC-AUC score of 91.47% then we are finding the threshold whereby ROC is the most optimal which is at 0.4088. By changing our threshold ROC-AUC score rises by 0.13% to 91.6%. There is **precision-recall tradeoff** observed as the False Negative reduces(140 to 127), the number of False Positive (73 to 85) is actually increasing. Comparing with the before and after threshold adjustment, precision 93.42% to 92.5% and recall from 88.1% to 89.2%.

- Depending on the post, our model count the frequency of words (or what we refer to as feature). **If the post contains a lot of vocabulary from the opposite class, our model is unable to predict correctly** just like in False Negative example.

- Last but not least, looking at the learning curve plot, we observe our Cross-Validation score has not reached plateau yet, which means we can try to **pull more training examples to improve our model score**.