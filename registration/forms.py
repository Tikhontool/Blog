from django import forms
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.models import User
from .models import MyUserCreationForm, MyPasswordChangeModel


class RegisterForm(MyUserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]





class MyPasswordChangeForm(MyPasswordChangeModel):

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]

class UserForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True, max_length=254)
    class Meta:
        model = User
        fields = ("email")