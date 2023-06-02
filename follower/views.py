from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from authentication.models import User

from follower.forms import FollowUsersForm


@login_required
def user_followed_by_user(request):
    pass


@login_required
def followers_of_user(request):
    pass


@login_required
def add_followed_user(request):
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
        "follower/add_followed_user.html",
        context={"form": form, "message": message},
    )


def follow_view(request):
    user = request.user
    personne_suivi_par_user = user.following.all()
    return render(
        request,
        "follower/follow_view.html",
        context={"personne_suivi_par_user": personne_suivi_par_user},
    )
