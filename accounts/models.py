from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20,unique=True,blank=True)

    def __str__(self):
        return self.nickname