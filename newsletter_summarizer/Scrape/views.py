from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import requests as Req , bs4
from .utils import head_function


# Create your views here.

def scrape_function(request):
    context = head_function()
    return render(request
                  ,template_name="home.html"
                  ,context=context)
    
def inovation(request):
    return render(request,template_name="inovation.html")

def sports(request):
    return render(request,template_name="sports.html")






