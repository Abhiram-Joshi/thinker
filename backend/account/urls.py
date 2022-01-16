from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^auth$", views.UserLoginAPIView.as_view(), name="user_login_signup"),
    re_path(r"^$", views.UserAPIView.as_view(), name="user_info_update"),
    re_path(r"^auth/refresh$", views.RefreshTokenAPIView.as_view(), name="refresh_token"),
]
