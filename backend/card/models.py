from django.db import models
from deck.models import Deck

# Create your models here.
class Card(models.Model):
    content = models.CharField(max_length=100)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)