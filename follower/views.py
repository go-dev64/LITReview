from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from follower.forms import FollowUsersForm


@login_required
def user_followed_by_user(request):
    pass


@login_required
def followers_of_user(request):
    pass


@login_required
def add_followed_user(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == "POST":
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(
        request, "follower/add_followed_user.html", context={"form": form}
    )
