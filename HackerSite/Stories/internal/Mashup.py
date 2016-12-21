import urllib.request
from django.db.models import Q
import json
import datetime
from ..models import Story

# fetches ids of all the top stories


def fetch_all_top_story_ids():
    print("fetching stories...")
    # stories = fetch_mashup_data("http://localhost/top-stories.json")
    stories = fetch_mashup_data(
        "https://community-hacker-news-v1.p.mashape.com/topstories.json")
    print("fetched stories.")
    return stories

# fetches the stories information


def fetch_stories(story_ids, offset, limit):
    stories_limited = story_ids[offset:(offset + limit)]
    missing_story_ids = []
    result = []
    index= offset

    for story_id in stories_limited:
        db_story = Story.objects.filter(id=story_id).first()
        if db_story is None:
            print("getting story data for {0}".format(story_id))
            story = fetch_story_details(story_id)
            print("getting sentiment data for Story#{0}".format(story_id))
            sentiment_analysis_result = get_setiment_analysis(story["title"])
            print("fetehcd#{0}".format(story_id))

            ob = {
                "title": story["title"], "author": story["by"], "url": story["url"] if ('url' in story) else "", "sentiment_confidence": sentiment_analysis_result['confidence'], "sentiment_result": sentiment_analysis_result['sentiment'], "id": story["id"], "score": story["score"], "timestamp": datetime.datetime.fromtimestamp(story["time"]).strftime('%Y-%m-%d %H:%M:%S')
            }
            db_story = Story.create(ob)
            db_story.save()

        index = index +1

        result.append({
            "index":index,
            "title": getattr(db_story, "title"), "author": getattr(db_story, "author"), "url": getattr(db_story, "url"), "id": getattr(db_story, "id"), "sentiment_result": getattr(db_story, "sentiment_result"), "sentiment_confidence": getattr(db_story, "sentiment_confidence"), "score": getattr(db_story, "score"), "timestamp": getattr(db_story, "timestamp"), "sentiment_smiley": "😊|😖"
        })


    return result

# fetches the stories info from Mashup Service


def fetch_story_details(id):
    story = fetch_mashup_data(
        "https://community-hacker-news-v1.p.mashape.com/item/{0}.json".format(id))
    return story


def get_setiment_analysis(title):
    return fetch_mashup_data("https://community-sentiment.p.mashape.com/text/", {
        "txt": title
    })["result"]

# fetches the data from Mashup API service


def fetch_mashup_data(url, req_data=None):
    try:
        headers = {
            "X-Mashape-Key": "XFADzyrUl5mshnDe4hBauHTDkZYPp1drg5vjsntTcZ8sBDnOyA",
            "Accept": "application/json"
        }
        if req_data is None:
            req = urllib.request.Request(url, headers=headers)
        else:
            data = urllib.parse.urlencode(req_data)
            data = data.encode('ascii')
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            req = urllib.request.Request(url, data, headers=headers)

        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')

        return json.loads(the_page)

    except Exception as e:
        raise

    return None
