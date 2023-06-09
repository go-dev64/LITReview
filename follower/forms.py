from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django import forms


class FollowUsersForm(forms.Form):
    user_to_follow = forms.CharField(
        max_length=63,
        label="Suivre un nouvel utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter le nom de l'utilisateur",
                "aria-label": "Entrer le nom de l'utilisateur",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FieldWithButtons(
                "user_to_follow",
                StrictButton("Envoyer", type="submit", css_class="btn btn-outline-secondary"),
                input_size="input-group-sm",
            ),
        )


class DeleteFollowUserForm(forms.Form):
    delete_followed_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)
