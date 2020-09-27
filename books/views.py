from django.shortcuts import render


# Create your views here.
def showBooks(request):
    return render(
        request,
        "books/books.html",
        {"name": request.session["name"]},
    )
