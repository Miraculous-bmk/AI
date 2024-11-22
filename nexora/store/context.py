from .forms import SubscriptionForm 


def newsletter_form(request):
    return {
        'form': SubscriptionForm(),
    }
