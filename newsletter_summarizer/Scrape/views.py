from django.shortcuts import render
from django.views.decorators.cache import cache_page
import asyncio
from .utils import main

# Create your views here.

# @cache_page(60 * 30)
# def scrape_function(request):
#     context = head_function()
#     return render(request
#                   ,template_name="home.html"
#                   ,context=context)


@cache_page(60 * 30)
def scrape_function(request):
    context = asyncio.run(main())
    return render(request
                  ,template_name="home.html"
                  ,context=context)


def inovation(request):
    return render(request,template_name="inovation.html")


def sports(request):
    return render(request,template_name="sports.html")

