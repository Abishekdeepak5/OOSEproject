# forms.py
from django import forms

class MyForm(forms.Form):
    my_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
