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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    PasswordChangeDoneView,
)
from django.shortcuts import redirect
from django.urls import path, include
from allauth.account import views as account_views
from authentication import views as auth_views
from post import views as post_views

urlpatterns = [
    path("admin/", admin.site.urls),
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
        "profile_photo",
        auth_views.upload_profile_photo,
        name="upload_profile_photo",
    ),
    path("home/", post_views.home, name="home"),
    path("photo/upload/", post_views.photo_uploader, name="photo_upload"),
    path(
        "post/create-ticket/", post_views.create_ticket, name="create_ticket"
    ),
    path(
        "post/<int:ticket_id>/edit", post_views.edit_ticket, name="edit_ticket"
    ),
    path("post/<int:ticket_id>", post_views.view_ticket, name="view_ticket"),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
