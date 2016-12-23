from django.db import models

class StoryManager(models.Manager):

    def create_story(self, details):
        story = self.create(
            title = details.title
            ,by  = details.by
            ,url = details.url
            ,id = details.id
            ,desc = details.desc
            ,score = details.score
            ,sentiment_confidence = details.sentiment_confidence
            ,sentiment_result = details.sentiment_result
            ,timestamp = details.timestamp)

        # do something with the story

        return story

class Story(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    by = models.CharField(max_length=100, help_text = "author", verbose_name="author")
    url = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    desc = models.TextField()
    sentiment_confidence = models.FloatField()
    sentiment_result = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    @classmethod
    def create(self, details):
        story = self(
            title = details["title"]
            ,by  = details["by"]
            ,url = details["url"]
            ,id = details["id"]
            ,desc = details["desc"]
            ,score = details["score"]
            ,sentiment_confidence=details["sentiment_confidence"]
            ,sentiment_result=details["sentiment_result"]
            ,timestamp = details["timestamp"])
        # do something with the story
        return story

    # objects = StoryManager()
