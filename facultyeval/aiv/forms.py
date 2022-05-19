from django import forms
from .models import *

class AIVRatingForm(forms.ModelForm):

    class Meta:

        model = AIVRating
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AIVRatingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"name": field, "class": "form-control"})

class AIVCriterionScoresForm(forms.Form):

    first_visit = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    second_visit = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    average_score = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    remarks = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
