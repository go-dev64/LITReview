from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = [
            "title",
            "description",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "rating",
            "headline",
            "body",
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ["image", "caption"]
