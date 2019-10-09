# Django-HackerNews

**[Django-HackerNews](http://sam016.pythonanywhere.com/Stories/)** is a web application which lets user access the top news in HackerNews using their public community API in [mashape](https://www.mashape.com). It also displays the underlying sentiment of the article.

*It's not live on pythonanywhere.com anymore. Please feel free to clone and run it using the command below.*

## Functionality
  1. **Lists** the currently top trending articles on HN.
  1. **Sentiment**: For each of the top articles, provides an additional visual aid which tells the viewer whether the article has a positive sentiment or not.  
  Sentiment is judged on the basis of the title of the article.
  1. **Storage**: Stores the article details and sentiment once fetched from RESTful service.

## RESTful services

[Mashape](https://www.mashape.com/) offers paid and free API and microservices to individuals, communities and organizations.  

Here are some APIs that Django-HackerNews application is consuming from Mashape:
  1. [Hacker News APIs](https://market.mashape.com/community/hacker-news)  
   1. to get the top stories
   1. to get a story details (title, author, score/upvotes, url, timestamp, comments, description)

  1. [Sentiment](https://www.mashape.com/vivekn/sentiment-3)
   1. to perform the sentiment analysis on the article

## Languages/Technologies
  1. python 3.5.2
  1. django 1.9.8

## How to execute
    python manage.py runserver [address = 127.0.0.1:8000]

#### Happy open-sourcing!!! :open_hands: ####
