from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder":"First Name"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder":"Last Name"})
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder":"Email Address"})
        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Username"})
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirm Password"})