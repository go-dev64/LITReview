from crispy_forms.helper import FormHelper
from django import forms
from .form_layouts import TicketFormLayout, ReviewFormLayout

from . import models


class TicketForm(forms.ModelForm):
    """form of create and edit ticket

    Args:
        forms (_type_):Model form => Object Ticket
    """

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
    """form of delete ticket

    Args:
        forms (_type_): _description_
    """

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    """form of create review with a new ticket, create review of existing ticket and edit review

    Args:
        forms (_type_): Model form => Object Review
    """

    RATING = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True, required=False)

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
    """form of delete Review

    Args:
        forms (_type_): _description_
    """

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class PhotoForm(forms.ModelForm):
    """form add or edit photo to ticket

    Args:
        forms (_type_): _description_
    """

    class Meta:
        model = models.Photo
        fields = [
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
