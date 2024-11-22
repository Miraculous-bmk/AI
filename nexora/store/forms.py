from django import forms
from .models import NewsletterSubscriber, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import CustomPasswordValidator

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

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search Nexora', 'class': 'nav-input'})
    )
    category = forms.ChoiceField(
        choices=[('all', 'All Collection')] + Product.CATEGORY_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'option-bar nav-left'})
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, validators=[CustomPasswordValidator])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'first_name', 'last_name', 'profile_picture', 'address']
        
