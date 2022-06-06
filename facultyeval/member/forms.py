from django import forms

class EditProfileForm(forms.Form):

    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    middle_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))