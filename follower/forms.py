from cProfile import label
from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUsersForm(forms.Form):
    user_to_follow = forms.CharField(
        max_length=63,
        label="Suivre un nouvel utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom de l'utilisateur",
                "aria-label": "Nom de l'utilisateur",
                "aria-describedby": "button-addon2",
            }
        ),
    )


class DeleteFollowUserForm(forms.Form):
    delete_followed_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)
