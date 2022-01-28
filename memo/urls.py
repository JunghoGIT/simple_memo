
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'memo'

urlpatterns = [
    path('', views.memo_list)
]

