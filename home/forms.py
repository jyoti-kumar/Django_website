from home.models import UserProfile
#from django.contrib.auth.models import User
from django import forms

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')
   