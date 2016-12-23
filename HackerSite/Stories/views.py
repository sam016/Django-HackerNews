from django.shortcuts import render
from django.http import HttpResponse
from .internal.stories import get_stories
from math import ceil
from .models import Story


# Create your views here.
def index(request):
    active_page = int(request.GET.get('page', '1'))

    stories = get_stories((active_page - 1) * 10, 10)

    # minimum page in pagination to show
    min_page_set = max(1, active_page - 2)

    # maximum page in pagination to show
    max_page_set = min(min_page_set + 4, ceil(stories["total"] / 10))

    # pages to show in pagination
    pages = range(min_page_set, max_page_set + 1)

    context = {
        "title": "Hacker News",
        "stories": stories["items"],
        "total": stories["total"],
        "pages": pages,
        "has_pages": len(pages)>0,
        "active_page": active_page,
        "prev_page": active_page - 1 if active_page > 1 else False,
        "next_page": active_page + 1 if (active_page)*10 < stories["total"] else False,
    }

    return render(request, "stories.html", context)


def search(request, query):
    active_page = int(request.GET.get('page', '1'))

    filtered_stories = Story.objects.filter(
        title__contains=query)[(active_page - 1) * 10:(active_page * 10)]

    stories = {
        "items": filtered_stories,
        "total": len(filtered_stories)
    }

    # minimum page in pagination to show
    min_page_set = max(1, active_page - 2)

    # maximum page in pagination to show
    max_page_set = min(min_page_set + 4, ceil(stories["total"] / 10))

    # pages to show in pagination
    pages = range(min_page_set, max_page_set + 1)

    context = {
        "title": "Hacker News",
        "stories": stories["items"],
        "total": stories["total"],
        "pages": pages,
        "has_pages": len(pages)>0,
        "search_query": query,
        "active_page": active_page,
        "prev_page": active_page - 1 if active_page > 1 else False,
        "next_page": active_page + 1 if (active_page)*10 < stories["total"] else False,
    }

    return render(request, "stories.html", context)
