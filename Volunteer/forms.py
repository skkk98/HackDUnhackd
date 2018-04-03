from django import forms
from .models import Feedback
class FeedbackForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please give a feedback'}))
    class Meta:
        model = Feedback
        fields = ['review']
