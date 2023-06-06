from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUsersForm(forms.Form):
    user_to_follow = forms.CharField(max_length=63, label="Nom de l'utilisateur à suivre")


class DeleteFollowUserForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
