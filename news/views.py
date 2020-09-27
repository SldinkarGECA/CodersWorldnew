from django.shortcuts import render

import requests
from .models import News


def news(request):
    # News.objects.all().delete()
    # url = "https://newsapi.org/v2/everything?q" \
    #       "=google" \
    #       "&sortBy=popularity&apiKey=3a84486c8e814609a943c709c7f93453"
    # open_bbc_page = requests.get(url).json()
    # article = open_bbc_page["articles"]
    # for i in article:
    #     # print(i["title"])
    #     news = News()
    #     news.title = i["title"]
    #     news.urlToImage = i["urlToImage"]
    #     news.url = i["url"]
    #     news.save()

    article = News.objects.all()
    return render(
        request,
        "news/news.html",
        {"categories": article,
         "name": request.session["name"]},
    )
