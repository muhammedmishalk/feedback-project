from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'mobile', 'email', 'rating', 'comments']

    # Use RATING_CHOICES from the model
    rating = forms.ChoiceField(choices=Feedback.RATING_CHOICES, widget=forms.RadioSelect)
