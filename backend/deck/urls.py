from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r"^get_topics", views.TopicAPIView.as_view(), name="get_all_deck_topics"),
    re_path(r"^create", views.DeckAPIView.as_view(), name="create_deck"),
    re_path(r"^update", views.DeckAPIView.as_view(), name="update_deck"),
    re_path(r"^delete", views.DeckAPIView.as_view(), name="delete_deck"),
    re_path(r"^get", views.DeckAPIView.as_view(), name="get_deck"),
    re_path(r"^", include("card.urls")),
]
