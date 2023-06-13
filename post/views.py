from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value, Q
from django.shortcuts import get_object_or_404, redirect, render


from itertools import chain

from post import models

from . import forms


@login_required
def home(request):
    """Home view , display flux of user with post of user followed by user connected"""
    reviews = models.Review.objects.filter(Q(user=request.user) | Q(user__in=request.user.following.all()))
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    tickets = models.Ticket.objects.filter(Q(user=request.user) | Q(user__in=request.user.following.all())).exclude(
        review__in=reviews
    )
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )
    return render(
        request,
        "post/home.html",
        context={
            "posts": posts,
        },
    )


@login_required
def create_ticket(request):
    """view of create new ticket

    Args:
        request (_type_): _description_

    Returns:
        _type_: New instance of Ticket Models
    """
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)

        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            if "image" not in photo_form:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
            else:
                photo = photo_form.save(commit=False)
                photo.uploader = request.user
                photo.save()
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.image = photo

            ticket.save()
            messages.success(request, f"tixket créée avec succés.")

            return redirect("home")

        else:
            messages.error(request)
            return redirect("post/create_ticket.html")

    my_forms = [ticket_form, photo_form]

    context = {"forms": my_forms}
    return render(request, "post/create_ticket.html", context=context)


@login_required
def edit_ticket(request, ticket_id):
    """View of edit Ticket. change or delete ticket

    Args:
        request (_type_): _description_
        ticket_id (_type_): id of ticket will be mofified

    Returns:
        _type_: Return instance modified
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    edit_photo = forms.PhotoForm(instance=ticket.image)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_photo = forms.PhotoForm(request.POST, instance=ticket.image)
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if all([edit_form.is_valid(), edit_photo.is_valid()]):
                if "image" not in edit_photo:
                    edit_form.save(commit=False)
                else:
                    photo = edit_photo.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
                    edit_form.image = photo

                edit_form.save()
                messages.success(request, f"Ticket modifié avec succés.")
                return redirect("home")

        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                messages.success(request, f"Ticket supprimé avec succés.")
                return redirect("home")

    my_forms = [edit_form, edit_photo]
    context = {
        "ticket": ticket,
        "forms": my_forms,
        "delete_form": delete_form,
    }
    return render(request, "post/edit_ticket.html", context=context)


@login_required
def create_review(request):
    """view of create a new ticket with this review

    Args:
        request (_type_): _description_

    Returns:
        _type_: New instance of Ticket Models linked wityh a new instance of Review
    """
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
            if "image" not in photo_form:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
            else:
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
            messages.success(request, f"Critique publiée avec succés.")
            return redirect("home")

    my_forms = [ticket_form, photo_form, review_form]

    context = {"forms": my_forms}
    return render(request, "post/create_review.html", context=context)


@login_required
def review_ticket(request, ticket_id):
    """View of review a already existing ticket

    Args:
        request (_type_): _description_
        ticket_id (_type_): id of ticket will be reviewed

    Returns:
        _type_: Return instance review
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            messages.success(request, f"Critique publiée avec succés.")
            return redirect("home")

    context = {
        "ticket": ticket,
        "forms": review_form,
    }
    return render(request, "post/review_ticket.html", context=context)


@login_required
def edit_review(request, review_id):
    """View of edit Review. change or delete Review

    Args:
        request (_type_): _description_
        ticket_id (_type_): id of Review will be mofified

    Returns:
        _type_: Return instance modified of review
    """
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReview()
    if request.method == "POST":
        if "body" in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                review_modified = edit_form.save(commit=False)
                review_modified.save()
                messages.success(request, f"Critique publiée avec succés.")
                return redirect("home")
            else:
                messages.error(request, edit_form.errors)
                return redirect("post/edit_review.html")

        if "delete_review" in request.POST:
            delete_form = forms.DeleteReview(request.POST)
            if delete_form.is_valid():
                review.delete()
                messages.success(request, f"Critique supprimée avec succés.")
                return redirect("home")

    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
        "review": review,
    }
    return render(request, "post/edit_review.html", context=context)


def view_user_posts(request):
    """view of element posted by the user connected

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    reviews = models.Review.objects.filter(user=request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    tickets = models.Ticket.objects.filter(user=request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )
    return render(request, "post/view_user_posts.html", context={"posts": posts})
