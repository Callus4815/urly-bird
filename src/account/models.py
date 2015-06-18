from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import messages
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)


    def __str__(self):
        return self.user


