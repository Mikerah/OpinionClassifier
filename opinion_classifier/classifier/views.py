from django.shortcuts import render

def index(request):
    """
    Takes user to the main index page.
    """
    render(request, 'classifier/index.html')
    
