from django.urls import path
from . import views

urlpatterns = [
    path("follower_page/", views.follower_page, name="follower_page"),
    path("follow/<int:user_follow_id>/delete/", views.delete_user_follow, name="delete_user_follow"),
]
