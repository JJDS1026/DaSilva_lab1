#forms.py

from django import forms

class IndexCardForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
