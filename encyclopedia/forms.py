from typing import ContextManager
from django import forms
from django.forms.widgets import Textarea

class NewEntryForm(forms.Form):
    title=forms.CharField (label="Заголовок")
    content=forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'row': 20}), label="Нова стаття")


