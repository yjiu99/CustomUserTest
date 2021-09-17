from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    email = models.EmailField(max_length=128,null=True)
    phonenumber = models.TextField(max_length=24,null=True)
    

