from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Memo(models.Model):

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


