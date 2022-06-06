from django import forms
from accounts.models import *
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class EditMemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ["middle_name", "image"]