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

class HRCriterionScoresForm(forms.ModelForm):

    class Meta:
        model = HRCriterionScores
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HRCriterionScoresForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"name": field, "class": "form-control"})