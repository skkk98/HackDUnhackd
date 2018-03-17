from django import forms
from .models import Event
class EventForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Event
        fields = ['image', 'title', 'description', 'place', 'contact']
