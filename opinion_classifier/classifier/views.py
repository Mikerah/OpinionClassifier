from django.shortcuts import render
from django.http import HttpResponseRedirect

from selenium import webdriver

import subprocess

from .forms import ArticleForm
from .models import Article

from .classifier import classifiers_predictions

def index(request):
    """
    Takes user to the main index page.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
                
            # Retrieve article
            url = form.cleaned_data['article_url']
            
            # Create Article model instance
            article = Article(url=url)
            
            # Initiate selenium webdriver
            driver = webdriver.FireFox()
            
            # Go to url
            driver.get(url)
            
            # Get type of article
            article.type = driver.find_element_by_xpath('//meta[@property="article:top-level-section"]/@content')
            # Get article title
            article.title = driver.find_element_by_xpath('//meta[@name="hdl"]/@content')
            # Get article author
            article.author = driver.find_element_by_xpath('//meta[@name="author"]/@content')
            # Get article text
            article.text = driver.find_element_by_xpath('//p')
            
            # Save article to database
            article.save()
            
            # store url in session
            request.session['article_url'] = url
            
            
            return HttpResponseRedirect('/results.html')
    else:
        form = ArticleForm()
        
    return render(request, 'classifier/index.html', {'form': form})
            
def results(request):
    article_url = request.session['article_url']
    article = Article.object.get(url=article_url)
    
    # clean article text
    new_text = article.text.replace('Advertisement',"",1).replace("We’re interested in your feedback on this page.","")
    article.text = new_text
    
    # Get predictions
    predictions = classifiers_predictions(article.text)
    
    return render(request, 'classifier/results', {'predictions': predictions})
    
def report(request):
    return render(request, 'classifier/report.html')
            
            
            
            
            
            
