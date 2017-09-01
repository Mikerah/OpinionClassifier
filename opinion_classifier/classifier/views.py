from django.shortcuts import render

def index(request):
    render(request, 'classifier/index.html')
    
