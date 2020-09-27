from django.shortcuts import render

from .models import Homepage


def homepage(request):
    request.session['name'] = None
    categories = Homepage.objects.all()
    return render(
        request,
        "homepage/homepage.html",
        {"categories": categories,
         "name": request.session["name"]},
    )
