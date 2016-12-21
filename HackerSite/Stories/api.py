from tastypie.resources import ModelResource
from .models import Story


class StoryResource(ModelResource):
    class Meta:
        limit = 10
        queryset = Story.objects.all()
        resource_name = 'story'
