from ast import Div
from logging import PlaceHolder
from turtle import title
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUsersForm(forms.Form):
    user_to_follow = forms.CharField(
        max_length=63,
        label="Entrer le nom de l'utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom de l'utilisateur",
                "aria-label": "Entrer le nom de l'utilisateur",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Suivre un nouvel utilisateur",
                FieldWithButtons(
                    "user_to_follow",
                    StrictButton("Envoyer", type="submit", css_class="btn btn-outline-secondary"),
                    input_size="input-group-sm",
                ),
            ),
        )


class DeleteFollowUserForm(forms.Form):
    delete_followed_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)
