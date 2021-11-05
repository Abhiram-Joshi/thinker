from django.db import models
from account.models import User

# Create your models here.
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=1000)
    image = models.URLField()
    views = models.PositiveIntegerField(default=0)