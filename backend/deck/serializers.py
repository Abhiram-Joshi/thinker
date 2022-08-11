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
    bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Deck
        exclude = ["reported", "bookmarked_by",]

    def get_bookmarked(self, obj):
        if self.context.get('request').user in obj.bookmarked_by.all():
            return True
        
        else:
            return False