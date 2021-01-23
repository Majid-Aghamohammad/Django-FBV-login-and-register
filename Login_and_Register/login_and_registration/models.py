# Create your models here.
# users/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfileInfo(models.Model):
    # add additional fields in here
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50, blank=True,null=False)
    last_name= models.CharField(max_length=50, blank=True ,null=False)
    def __str__(self):
        return self.user.username
