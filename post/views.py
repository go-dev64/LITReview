from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from post import models

from . import forms


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(
        request,
        "post/home.html",
        context={"tickets": tickets, "reviews": reviews},
    )


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.image = photo
            ticket.save()
            return redirect("home")

    context = {"ticket_form": ticket_form, "photo_form": photo_form}
    return render(request, "post/create_ticket.html", context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")

        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("home")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "post/edit_ticket.html", context=context)


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(
        request,
        "post/view_ticket.html",
        {
            "ticket": ticket,
        },
    )


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all(
            [
                ticket_form.is_valid(),
                photo_form.is_valid(),
                review_form.is_valid(),
            ]
        ):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.image = photo
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")

    context = {
        "ticket_form": ticket_form,
        "photo_form": photo_form,
        "review_form": review_form,
    }
    return render(request, "post/create_review.html", context=context)


@login_required
def review_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")

    context = {
        "ticket": ticket,
        "review_form": review_form,
    }
    return render(request, "post/review_ticket.html", context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Ticket, id=review_id)
    return render(request, "post/view_review.html", {"review": review})


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
