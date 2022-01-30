from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label='닉네임')

    class Meta:
        model = Profile
        fields = [
            'nickname',
            ]

    def clean_nickname(self):
        nickname= self.cleaned_data['nickname']
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("사용중인 닉네임 입니다.")
        else :
            return nickname