from django.db import models
from django.contrib.auth.models import User


class SubscribedUsers(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=45, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
