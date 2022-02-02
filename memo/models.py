from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Profile

# Create your models here.


class Memo(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, to_field= 'nickname')
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)


