from django.conf.urls import url
from . import views

urlpatterns = [
    url("^get_topics", views.TopicAPIView.as_view(), name="get_all_deck_topics"),
    url("^create", views.DeckAPIView.as_view(), name="create_deck"),
]