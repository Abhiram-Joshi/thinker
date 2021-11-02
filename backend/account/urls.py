from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^auth/$", views.UserLoginAPIView.as_view(), name="user_login_signup"),
    url(r"^auth/refresh$", views.RefreshTokenAPIView.as_view(), name="refresh_token"),
]
