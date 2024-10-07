from django.db import models

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    channels = models.CharField(max_length=255)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
