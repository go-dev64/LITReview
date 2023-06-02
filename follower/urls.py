from django.urls import path
from . import views

urlpatterns = [
    path(
        "follower-users/",
        views.add_followed_user,
        name="add_followed_user",
    ),
    path("follow_view/", views.follow_view, name="follow_view"),
]
