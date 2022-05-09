from django.forms import ModelForm
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