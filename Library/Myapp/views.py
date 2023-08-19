from webbrowser import Elinks
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from Books.models import books
from Movies.models import movies

def index(request):
    return render(request, "Myapp/index.html", {
        'b': books.objects.latest('id'),
        'm':movies.objects.latest('id'),
        'm2': movies.objects.latest('title'),
        })
