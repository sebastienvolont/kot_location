from django import forms

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import KotOwner, Kot, User


class KotOwnerForm(forms.ModelForm):
    class Meta:
        model = KotOwner
        fields = '__all__'


class KotForm(forms.ModelForm):
    class Meta:
        model = Kot
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'user_type']
