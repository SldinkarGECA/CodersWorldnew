from django.shortcuts import render

# Create your views here.
def showBlogs(request):
    return render(
        request,
        "blogs/blogs.html",
        {"name": request.session["name"]},
    )