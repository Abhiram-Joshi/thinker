from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^(?P<deck_id>[0-9]+)/cards", views.CardsAPIView.as_view(), name="get_card_data"),
    url(r"^cards/(?P<id>[0-9]+)", views.CardsDeleteAPIView.as_view(), name="get_card_data"),
]