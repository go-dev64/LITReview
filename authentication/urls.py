from django.urls import path
from allauth.account import views as account_views
from django.contrib.auth.views import (
    PasswordChangeDoneView,
)
from allauth.account import views as account_views
from . import views

urlpatterns = [
    path(
        "",
        account_views.LoginView.as_view(
            template_name="authentication/login.html",
        ),
        name="login",
    ),
    path(
        "accounts/signup/",
        account_views.SignupView.as_view(
            template_name="authentication/signup.html",
        ),
    ),
    path(
        "accounts/logout/",
        account_views.LogoutView.as_view(
            template_name="authentication/logout.html"
        ),
        name="account_logout",
    ),
    path(
        "accounts/password/change/",
        account_views.PasswordChangeView.as_view(
            template_name="authentication/change_password.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/change_password_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "profile_photo/",
        views.upload_profile_photo,
        name="upload_profile_photo",
    ),
]
