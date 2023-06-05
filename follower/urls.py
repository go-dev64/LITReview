from django.urls import path
from . import views

urlpatterns = [
    path("follow_view/", views.follower_views, name="follower_view"),
]
