from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your models here.



class Account(models.Model):
    user = models.OneToOneField(User)



    def __str__(self):
        return self.user



def validate_date_in_past(value):
    if value >= date.today():
        raise ValidationError("Date must be in past.")

class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True, blank=True,
                                validators=[validate_date_in_past])


    def __str__(self):
        return str(self.user)

