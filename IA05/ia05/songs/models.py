from django.db import models
from django.urls import reverse

class Song(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def get_absolute_url(self):
        return reverse("song:detail", kwargs={"pk": self.pk})
