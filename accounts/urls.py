from allauth.socialaccount.providers.google.views import oauth2_login
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', oauth2_login, name='login'),
    path('nickname/', views.create_nickname, name='create_nickname'),
    path('logout/', views.logout, name='logout')

]
