from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import requests as Req , bs4



# Create your views here.

def head_function(request):
    url = "https://www.bbc.com/"
    response = Req.get(url).text
    soup = bs4.BeautifulSoup(response, "html.parser")
    tag_a = soup.select('a')
    head = []
    para = []
    image = []
    for elements in tag_a:
        h2 = elements.select("h2")
        p = elements.select("p")
        img = elements.select('img[src]')
        if h2 and p:
            head.append(h2[0].getText())
            para.append(p[0].getText())
            if img:
                image.append(img[1]['src'])
            else:
                image.append(r"https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")
    news = zip(head,para,image)
    context = {
        "news_items":news
    }

    return render(request
                  ,template_name="home.html"
                  ,context=context)








