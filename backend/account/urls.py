from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^auth$", views.UserLoginAPIView.as_view(), name="user_login_signup"),
    url(r"^$", views.UserAPIView.as_view(), name="user_info_update"),
    url(r"^auth/refresh$", views.RefreshTokenAPIView.as_view(), name="refresh_token"),
]
