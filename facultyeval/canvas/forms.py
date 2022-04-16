from django import forms
from .models import MGRating

class EvaluationForm(forms.ModelForm):

    class Meta:
        model = MGRating
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EvaluationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"class":"form-control"})