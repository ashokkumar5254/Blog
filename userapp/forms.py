from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel

class signup_form(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''  # Remove help_text for username
        self.fields['password1'].help_text = ''  # Remove help_text for password1
        self.fields['password2'].help_text = ''  # Remove help_text for password2
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Remove help_text for username
        self.fields['email'].help_text = ''
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=('image',)
