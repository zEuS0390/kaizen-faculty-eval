from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class SchoolYearForm(ModelForm):

    class Meta:

        model = SchoolYear
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SchoolYearForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"name": field, "class": "form-control"})

class EditUserForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})