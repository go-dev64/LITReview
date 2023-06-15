from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from authentication.models import User

from follower.forms import FollowUsersForm, DeleteFollowUserForm


@login_required
def follower_page(request):
    request.user.user_followed_by_user_and_followers()
    if request.method == "POST":
        form = FollowUsersForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data["user_to_follow"]
        try:
            user_to_follow = get_object_or_404(User, username=form)
        except:
            messages.error(request, f"Utilisateur inconnue. Merci de renseigner un utilisateur connue!")
            return redirect("follower_page")
        else:
            request.user.following.add(user_to_follow)
            messages.success(request, f"{user_to_follow} a été ajouté avec succes aux utilisateurs que vous suivez.")
            return redirect("follower_page")
    form = FollowUsersForm()
    return render(
        request,
        "follower/follower_page.html",
        context={
            "form": form,
            "user_followed_by_user": request.user.user_followed_by_user,
            "followers": request.user.followers_of_user,
        },
    )


def delete_user_follow(request, user_follow_id):
    delete_form = DeleteFollowUserForm()
    if request.method == "POST":
        if "delete_followed_user" in request.POST:
            delete_form = DeleteFollowUserForm(request.POST)
            if delete_form.is_valid():
                user_follow = request.user.delete_user_follow(user_follow_id)
                messages.success(
                    request, f"{user_follow} a été supprimé avec succes de la liste des utilisateurs que vous suivez."
                )
                return redirect("follower_page")
    else:
        delete_form = DeleteFollowUserForm()
    return render(
        request,
        "follower/delete_user_follow.html",
        {
            "delete_form": delete_form,
        },
    )
