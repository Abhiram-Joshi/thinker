from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^get_topics", views.TopicAPIView.as_view(), name="get_all_deck_topics"),
    url(r"^create", views.DeckAPIView.as_view(), name="create_deck"),
    url(r"^update/(?P<id>[0-9]+)", views.DeckAPIView.as_view(), name="update_deck"),
    url(r"^delete/(?P<id>[0-9]+)", views.DeckAPIView.as_view(), name="delete_deck"),
]
