from django.db import models
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(max_length=200)
    away = models.CharField(max_length=200)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title