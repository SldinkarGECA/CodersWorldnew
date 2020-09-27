from django.shortcuts import render
from .models import Book

# Create your views here.
def showBooks(request):
    allBooks = Book.objects.all();

    return render(request, "books/books.html", {"name": request.session["name"], "allBooks": allBooks})
