from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import requests as Req , bs4



# Create your views here.
def head_function(request):
    url = "https://www.bbc.com/"
    response = Req.get(url).text
    soup = bs4.BeautifulSoup(response,"html.parser")
    headings = soup.find_all("h2")
    paragraphs = soup.find_all("p")
    img = soup.find_all("img")
    sourse = [x.get("src") for x in img]
    image_urls = sourse[1::2]
    headlines = [heading.getText(strip=True) for heading in headings]
    paragraphs_list = [para.getText(strip=True) for para in paragraphs]
    news = zip(headlines,paragraphs_list,image_urls) #zip refer google or tuple unpacking
    context = {
        "news_items": news,
        # "image": image_urls
    }
    return render(request
                  ,template_name="home.html"
                  ,context=context)

