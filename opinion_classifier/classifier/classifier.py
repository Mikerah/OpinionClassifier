from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from .misc import create_data

def classifiers_predictions(article_text):
    """
    Given an article, returns the prediction of its category from Naive Bayes, Logistic Regression, Random Forests and Decision Trees
    :param article text str
    """
    # Retrieve data 
    data = create_data()
    
    # Initialize Pipelines
    pipeline_nb = Pipeline([('vectorizer', TfidfVectorizer()), ('classifier', MultinomialNB())])
    pipeline_lr = Pipeline([('vectorizer', TfidfVectorizer()), ('classifier', LogisticRegression())])
    pipeline_rf = Pipeline([('vectorizer', TfidfVectorizer()), ('classifier', RandomForestClassifier())])
    pipeline_dt = Pipeline([('vectorizer', TfidfVectorizer()), ('classifier', DecisionTreeClassifier())])
    
    # Fit data for each pipeline
    pipeline_nb.fit(data['text'], data['type'])
    pipeline_lr.fit(data['text'], data['type'])
    pipeline_rf.fit(data['text'], data['type'])
    pipeline_dt.fit(data['text'], data['type'])
    
    # Store predictions in results dictionary and return the dictionary
    predictions = {'Naive Bayes': 0, 'Logistic Regression': 0, 'Random Forests': 0, 'Decision Trees': 0}
    predictions['Naive Bayes'] = pipeline_nb.fit(article_text)[0]
    predictions['Logistic Regression'] = pipeline_lr.fit(article_text)[0]
    predictions['Random Forests'] = pipeline_rf.fit(article_text)[0]
    predictions['Decision Trees'] = pipeline_dt.fit(article_text)[0]
    
    return predictions
    
    
    


        
        
        
    
        
    
        

