from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from authentication.models import User

from follower.forms import FollowUsersForm, DeleteFollowUserForm
from . import forms
from . import models


def user_followed_by_user_and_followers(request):
    user = request.user
    user_followed_by_user = user.following.all()
    followers = user.followers.all()

    return user_followed_by_user, followers


@login_required
def follower_page(request):
    user_followed_by_user, followers = user_followed_by_user_and_followers(request=request)
    form = FollowUsersForm()
    message = ""
    if request.method == "POST":
        form = FollowUsersForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data["user_to_follow"]
            try:
                user_to_follow = User.objects.get(username=form)
            except:
                message = f"Utilisateur inconnue"
            else:
                request.user.following.add(user_to_follow)
                return redirect("home")

    return render(
        request,
        "follower/follower_page.html",
        context={
            "form": form,
            "message": message,
            "user_followed_by_user": user_followed_by_user,
            "followers": followers,
        },
    )


def delete_user_follow(request, user_follow_id):
    user = request.user
    user_follow = get_object_or_404(models.UserFollows, followed_user=user_follow_id)
    delete_form = DeleteFollowUserForm()
    if "delete_followed_user" in request.POST:
        delete_form = DeleteFollowUserForm(request.POST)
        if delete_form.is_valid():
            user.following.remove(user_follow.followed_user)
            return redirect("follower_page")
    return render(request, "follower/delete_user_follow.html", {"delete_form": delete_form})
