from django.db import models

from account.models import User


# Create your models here.
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=1000)
    image = models.URLField()
    views = models.PositiveIntegerField(default=0)
    wiki_url = models.URLField(default="https://en.wikipedia.org/wiki/Main_Page")
    image_url = models.URLField(default="https://www.designyourway.net/blog/wp-content/uploads/2017/12/open-uri20150521-11-1cr23xw.jpg")
    views = models.PositiveIntegerField(default=0)
    private = models.BooleanField(default=False)
    reported = models.BooleanField(default=False)
    bookmarks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    bookmarked_by = models.ManyToManyField(User, related_name="bookmarked_by", blank=True)
