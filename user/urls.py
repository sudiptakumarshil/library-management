from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserUpdateView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="auth.register"),
    path("login/", UserLoginView.as_view(), name="auth.login"),
    path("logout/", UserLogoutView.as_view(), name="auth.logout"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
]
