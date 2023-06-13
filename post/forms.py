from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Column, Row
from crispy_forms import bootstrap
from django import forms
from .form_layouts import TicketFormLayout, ReviewFormLayout

from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True, required=False)

    class Meta:
        model = models.Ticket
        fields = [
            "title",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Titre"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = TicketFormLayout()


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    RATING = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True, disabled=True)

    class Meta:
        model = models.Review
        fields = [
            "headline",
            "rating",
            "body",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["headline"].label = "Titre"
        self.fields["rating"] = forms.ChoiceField(choices=self.RATING, widget=forms.RadioSelect())
        self.fields["rating"].label = "Donner une note"
        self.fields["body"].label = "Commentaire"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = ReviewFormLayout()


class DeleteReview(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
