from django import forms
from .models import NewsletterSubscriber

class SubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email address',
        'required': 'required'
    }))
    channels = forms.MultipleChoiceField(
        choices=[
            ('all', 'Subscribe to All Channels'),
            ('news', 'News & Updates'),
            ('offers', 'Exclusive Offers'),
            ('events', 'Events & Webinars'),
            ('blog', 'Blog Updates'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if NewsletterSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        channels = cleaned_data.get('channels', [])
        
        if 'all' in channels:
            cleaned_data['channels'] = ['all']
        return cleaned_data
