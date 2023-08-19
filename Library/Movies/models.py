from django.db import models

class movies(models.Model):
    cover = models.ImageField(upload_to='static/img/movies')
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'moive'