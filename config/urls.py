"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path, include
from authentication import views as auth_views
from allauth.account import views as account_views
from post import views as post_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        account_views.LoginView.as_view(
            template_name="authentication/login.html",
            # redirect_authenticated_user=True,
        ),
        name="account_login",
    ),
    path(
        "accounts/logout/",
        account_views.LogoutView.as_view(),
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
    path("home/", post_views.home, name="home"),
    path("accounts/", include("allauth.urls")),
]
