from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import requests as Req , bs4
from transformers import pipeline



def head_function():
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
    return context

def summarize_function():
    summarizer = pipeline("summarization")
    article ="""Millions of people in the Middle East dream of safe, quiet lives without drama and violent death. The last year of war, as bad as any in the region in modern times, has shown yet again that dreams of peace cannot come true while deep political, strategic and religious fault lines remain unbridged. Once again, war is reshaping the politics of the Middle East.

The Hamas offensive came out of well over a century of unresolved conflict. After Hamas burst through the thinly defended border, it inflicted the worst day the Israelis had suffered.

Around 1,200 people, mostly Israeli civilians, were killed. Israel’s prime minister, Benjamin Netanyahu, phoned President Joe Biden and told him that “We’ve never seen such savagery in the history of the state”; not “since the Holocaust.” Israel saw the attacks by Hamas as a threat to its existence.

Since then, Israel has inflicted many terrible days on the Palestinians in Gaza. Nearly 42,000 people, mostly civilians have been killed, according to the Hamas-run health ministry. Much of Gaza is in ruins. Palestinians accuse Israel of genocide.

The war has spread. Twelve months after Hamas went on the offensive the Middle East is on the edge of an even worse war; wider, deeper, even more destructive."""
    summary = summarizer(article,max_length=120, min_length=80, do_sample=False)
    return summary