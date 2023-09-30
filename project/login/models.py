from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token

class CustomToken(Token):
    expiration_date = models.DateTimeField()

def update_token_expiration(token):
    # Set the expiration date to 30 days from now
    token.expiration_date = timezone.now() + timezone.timedelta(days=30)
    token.save()
