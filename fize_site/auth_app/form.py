from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore

class CustomUserCreationForm(UserCreationForm):
    password1: forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )  # type: ignore
    password2 : forms.CharField( # type: ignore
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip= False
    ) # type: ignore
class Meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ("password1", "password2")