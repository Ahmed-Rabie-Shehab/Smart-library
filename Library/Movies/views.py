from django.shortcuts import render
from .models import movies

def movie_view(request):
    return render(request, "Movies/movies.html", {'movie': movies.objects.all()})