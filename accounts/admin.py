from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile

# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass