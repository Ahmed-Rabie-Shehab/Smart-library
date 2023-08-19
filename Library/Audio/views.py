from django.shortcuts import render
from .models import audios

def audio_view(request):
    return render(request, "Audio/audio.html", {'audio': audios.objects.all()})