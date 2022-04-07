from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r"^get_topics/$", views.TopicAPIView.as_view(), name="get_all_deck_topics"),
    re_path(r"^create/$", views.DeckAPIView.as_view(), name="create_deck"),
    re_path(r"^update/$", views.DeckAPIView.as_view(), name="update_deck"),
    re_path(r"^delete/$", views.DeckAPIView.as_view(), name="delete_deck"),
    re_path(r"^get_created/$", views.DeckCreatedListAPIView.as_view(), name="get_all_decks"),
    re_path(r"^get/$", views.DeckAPIView.as_view(), name="get_deck"),
    re_path(r"^bookmark/$", views.DeckBookmarkAPIView.as_view(), name="bookmark_deck"),
    re_path(r"^remove_bookmark/$", views.DeckRemoveBookmarkAPIView.as_view(), name="remove_bookmark_deck"),
    re_path(r"^get_bookmarked_decks/$", views.GetBookmarkedDecksAPIView.as_view(), name="get_bookmarked_decks"),
    re_path(r"^home_feed/$", views.DeckHomeFeedListAPIView.as_view(), name="get_home_feed_decks"),
    re_path(r"^$", include("card.urls")),
]
