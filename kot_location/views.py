from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Kot, KotOwner
from .forms import KotOwnerForm, KotForm, RegisterForm


def home_page(request):
    return render(request, 'kot_location/home_page.html')


@login_required(login_url='/login')
def kot_list(request):
    all_kot = Kot.objects.all()
    return render(request, 'kot_location/kot_list.html', {'kots': all_kot})


def kot_add(request):
    if request.method == 'POST':
        form = KotForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get("location_start_date")
            end_date = form.cleaned_data.get("location_end_date")
            days_number = end_date - start_date
            if end_date > start_date:
                kot = form.save()
    else:
        form = KotForm()
    return render(request, 'kot_location/kot_add.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/kot_list')
        else:
            form = AuthenticationForm()
        return render(request, 'kot_location/login.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = UserCreationForm()
    return render(request, 'kot_location/register.html', {'form': form})


def is_active(request):
    if request.user.is_authenticated:
        is_connected = request.user.is_authenticated
        return HttpResponse('<h1> Authentifié </h1>')


def kot_details(request, id):
    kot = Kot.objects.get(id=id)
    return render(request, 'kot_location/kot_details.html', {'kot': kot})


def kot_delete(request, id):
    kot_to_delete = Kot.objects.get(id=id)
    if request.method == 'POST':
        kot_to_delete.delete()
        return redirect('/kot_list')

    return render(request, 'kot_location/kot_delete.html', {'kot_to_delete': kot_to_delete})
