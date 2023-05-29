from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from post import models

from . import forms


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, "post/home.html", context={"tickets": tickets})


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect("home")
    return render(request, "post/create_ticket.html", context={"form": form})


@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect("home")
    return render(request, "post/create_ticket.html", context={"form": form})


@login_required
def photo_uploader(request):
    form = forms.PhotoForm()
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect("home")
    return render(request, "post/photo_upload.html", context={"form": form})
