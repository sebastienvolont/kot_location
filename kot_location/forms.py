from django import forms

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Kot, User


class KotForm(forms.ModelForm):
    class Meta:
        model = Kot
        fields = '__all__'
        exclude = ('kot_owner',)


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'user_type')
