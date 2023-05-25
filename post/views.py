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
