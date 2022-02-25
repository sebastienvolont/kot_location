from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.messages import get_messages

from .models import Kot, KotOwner
from .forms import KotOwnerForm, KotForm, RegisterForm


def home_page(request):
    return render(request, 'kot_location/home_page.html')


def kot_list(request):
    all_kot = Kot.objects.all()
    return render(request, 'kot_location/kot_list.html', {'kots': all_kot})


@login_required(login_url='/login')
@permission_required('kot_location.add_kot', raise_exception=True)
def kot_add(request):
    if request.method == 'POST':
        form = KotForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get("location_start_date")
            end_date = form.cleaned_data.get("location_end_date")
            days_number = end_date - start_date
            if end_date > start_date:
                kot = form.save()
                messages.add_message(request, messages.SUCCESS, 'Annonce ajoutée !')
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
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = RegisterForm()
        if request.method == "POST":
            print("test")
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                if request.user.user_type == 'OWNER':
                    permission_owner = Permission.objects.get(codename='add_kot')
                    user.user_permissions.add(permission_owner)
                return redirect('/kot_list')
        else:
            form = RegisterForm()
        return render(request, 'kot_location/register.html', {'form': form})


def kot_details(request, id):
    kot = Kot.objects.get(id=id)
    return render(request, 'kot_location/kot_details.html', {'kot': kot})


def kot_delete(request, id):
    kot_to_delete = Kot.objects.get(id=id)
    if request.method == 'POST':
        kot_to_delete.delete()
        return redirect('/kot_list')

    return render(request, 'kot_location/kot_delete.html', {'kot_to_delete': kot_to_delete})


def kot_update(request, id):
    return HttpResponse('Page de modification')
