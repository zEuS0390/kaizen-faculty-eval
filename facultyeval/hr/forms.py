from django import forms
from .models import *

class HRRatingForm(forms.ModelForm):

    class Meta:
        model = HRRating
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HRRatingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"name": field, "class": "form-control"})

class HRCriterionScoresForm(forms.Form):

    program_chair_score = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    student_score = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    average_score = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    remarks = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
