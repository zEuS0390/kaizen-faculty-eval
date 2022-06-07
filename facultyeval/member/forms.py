from django import forms
from accounts.models import *
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})

class EditMemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ["middle_name", "image"]

    def __init__(self, *args, **kwargs):
        super(EditMemberForm, self).__init__(*args, **kwargs)
        self.fields["middle_name"].widget.attrs.update({"class":"form-control"})
        self.fields["image"].widget.attrs.update({"type": "file", "class":"form-control"})