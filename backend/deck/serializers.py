from rest_framework import serializers

from .models import Deck


class CreateDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        exclude = ["user", "views", "reported", "created_at"]

class UpdateDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        exclude = ["user", "views", "reported", "created_at", "topic", "wiki_url"]

class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        exclude = ["user", "reported"]