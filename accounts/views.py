from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from allauth.account.views import LoginView
from django.contrib.auth import logout as auth_logout

# Create your views here.

def create_nickname(request):
    if request.method == 'POST':
        profileform = ProfileForm(request.POST)
        if profileform.is_valid():
            profile = profileform.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('memo:index')
        else :
            return render(request, 'accounts/create_nickname.html', {
                'form': profileform
            })

    profileform =ProfileForm()

    return render(request, 'accounts/create_nickname.html',{
        'form' : profileform
    })


def logout(request):
    auth_logout(request)
    return redirect('memo:index')