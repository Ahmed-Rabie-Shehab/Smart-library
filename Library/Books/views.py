from django.shortcuts import render
from .models import books
def book_view(request):
    return render(request, "Books/books.html", {'book': books.objects.all()})