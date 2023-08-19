from django.db import models

class books(models.Model):
    cover = models.ImageField(upload_to='static/img/books')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'