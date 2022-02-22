from django import forms

from django.contrib.auth.models import User
from .models import KotOwner, Kot


class KotOwnerForm(forms.ModelForm):
    class Meta:
        model = KotOwner
        fields = '__all__'


class KotForm(forms.ModelForm):
    class Meta:
        model = Kot
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
