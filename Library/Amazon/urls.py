from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Myapp.urls"), name="home"),
    path("books/", include("Books.urls")),
    path("movies/", include("Movies.urls")),
    path("audio/", include("Audio.urls")),
    path("user/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
