from django.db import models

class StoryManager(models.Manager):

    def create_story(self, details):
        story = self.create(
            title = details.title
            ,author  = details.author
            ,url = details.url
            ,id = details.id
            ,score = details.score
            ,sentiment_confidence=details.sentiment_confidence
            ,sentiment_result=details.sentiment_result
            ,timestamp = details.timestamp)

        # do something with the story

        return story

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    sentiment_confidence = models.FloatField()
    sentiment_result = models.CharField(max_length=50)
    id = models.BigIntegerField(primary_key=True)
    score = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    @classmethod
    def create(self, details):
        story = self(
            title = details["title"]
            ,author  = details["author"]
            ,url = details["url"]
            ,id = details["id"]
            ,score = details["score"]
            ,sentiment_confidence=details["sentiment_confidence"]
            ,sentiment_result=details["sentiment_result"]
            ,timestamp = details["timestamp"])
        # do something with the story
        return story

    # objects = StoryManager()
