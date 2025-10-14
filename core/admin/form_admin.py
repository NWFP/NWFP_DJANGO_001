# admin.py
from django import forms
from django.contrib import admin
from django.forms.widgets import DateInput
from core.models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }
