# pip install joblib if not installed yet

import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') #base route
def load_webpage():
    return render_template('classification_input.html') #to render the input

@app.route('/reddit_input', methods = ['POST'])
#news input with method = post / get, when we trigger our function, we need the method to be post
def reddit_input():
	if request.method.lower() == 'post':
		detail = request.form['reddit'] #the request is to get it from form

	# clean news of punctuation and newlines(preprocessing)
	exclude = set(string.punctuation)
	detail = ''.join(char for char in detail if char not in exclude)
	detail = detail.replace('\n', '')

	# load trained model
	pipeline = joblib.load('pipe2cv.pkl') #importing the train model

	detail = [(detail)]
	output = pipeline.predict(detail) #predicting which category the new text belong to
     #to output in text html output
    return output

if __name__ == '__main__':
	app.run(debug = True)
