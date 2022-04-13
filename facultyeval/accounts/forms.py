from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

class PassResetForm(PasswordResetForm):

    email = forms.EmailField(
        label="Email Address",
        max_length=254,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email Address",
            "autocomplete": "email"})
    )

    def __init__(self, *args, **kwargs):
        super(PassResetForm, self).__init__(*args, **kwargs)

class UserForm(UserCreationForm):

    middle_name = forms.CharField(max_length=200, required=True, label="Middle Name")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2", "middle_name"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
        self.fields["middle_name"].widget.attrs.update({"class": "form-control", "placeholder":"Middle Name"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder":"Last Name"})
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder":"Email Address"})
        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Username"})
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirm Password"})