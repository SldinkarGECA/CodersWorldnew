from django.shortcuts import render

from .models import Course


# Create your views here.
def showCourses(request):
    allCourses = Course.objects.all()
    return render(
        request,
        "courses/courses.html",
        {"courses": allCourses,
         "name": request.session["name"]},
    )
