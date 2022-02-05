
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'memo'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/memo/<str:nickname>', views.memo_list, name='memo_list'),
    path('api/memo/<str:nickname>/<int:pk>', views.memo_detail, name='memo_detail'),
]

