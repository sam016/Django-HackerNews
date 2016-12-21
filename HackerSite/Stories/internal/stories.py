from . import Mashup


def get_stories(offset=0, limit=10):
    story_ids = Mashup.fetch_all_top_story_ids()
    stories = Mashup.fetch_stories(story_ids, offset, limit)
    return {"total": len(story_ids), "items": stories}
