from django.shortcuts import render
from django.http import HttpResponse


def contact_us(request):
    context = {
        "title": "Contact us"
    }
    return render(request, "contact_us.html", context)
    # return HttpResponse("Contact us")

def about_us(request):
    context = {
        "title": "About us"
    }
    return render(request, "about_us.html", context)
