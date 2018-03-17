from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminDateWidget
import datetime
class EventForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Event
        fields = ['image', 'title', 'description', 'place', 'contact', 'fro', 'to']
