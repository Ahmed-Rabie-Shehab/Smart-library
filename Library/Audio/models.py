from django.db import models

class audios(models.Model):
    cover = models.ImageField(upload_to='static/img/audios')
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    link = models.URLField(default='#')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Audio'