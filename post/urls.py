from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("ticket/create/", views.create_ticket, name="create_ticket"),
    path(
        "ticket/<int:ticket_id>/edit/",
        views.edit_ticket,
        name="edit_ticket",
    ),
    path(
        "ticket/<int:ticket_id>/review/",
        views.review_ticket,
        name="review_ticket",
    ),
    path("review/create/", views.create_review, name="create_review"),
    path(
        "review/<int:review_id>/edit",
        views.edit_review,
        name="edit_review",
    ),
    path(
        "view_user_posts/",
        views.view_user_posts,
        name="view_user_posts",
    ),
]
