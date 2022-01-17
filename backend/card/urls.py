from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^cards", views.CardsAPIView.as_view(), name="get_card_data"),
    re_path(r"^card", views.CardsDeleteAPIView.as_view(), name="get_card_data"),
]