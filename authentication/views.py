from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings


from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentication/signup.html", context={"form": form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    print(form)
    if request.method == "POST":
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Changement de votre photo de profile réalisé avec succés!")
            return redirect("home")
        else:
            messages.warning(request, "Please correct the error below.")

    return render(
        request,
        "authentication/edit_profile.html",
        context={"form": form, "title": "Changement photo de profile"},
    )


@login_required
def profile_view(request):
    return render(request, "authentication/profile_view.html", {"user": request.user})
