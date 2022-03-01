import datetime

from django.contrib import messages
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from .forms import KotForm, RegisterForm
from .models import Kot, KotAd


def home_page(request):
    """
    First page to introduce the kot rent location website
    @return:
    """
    return render(request, 'kot_location/home_page.html')


def kot_list(request):
    """
    Displays all kots ads available on the website approved by a superuser
    @return:
    """
    all_kot_ad = KotAd.objects.all()
    choice_fields = Kot._meta.get_field('kot_city').choices

    if request.POST and request.POST['price'] != '' and request.POST['city'] != '':
        return render(request, 'kot_location/kot_list.html',
                      {'kots': filter_kots(request, price_month__gte=request.POST['price'],
                                           kot_city=request.POST['city']), 'kots_ads': all_kot_ad,
                       'choice_fields': choice_fields})
    else:
        return render(request, 'kot_location/kot_list.html',
                      {'kots': filter_kots(request), 'kots_ads': all_kot_ad, 'choice_fields': choice_fields})


def filter_kots(request, **kwargs):
    """
    Permits to use filters on city location and prices by month from available Kots
    @return:
    """
    if request.method == "POST":
        all_kot = Kot.objects.all().filter(**kwargs)
        return all_kot
    else:
        all_kot = Kot.objects.all()
        return all_kot


def kot_details(request, id: int):
    """
    Displays detailed detailed view on a certain Kot by its id
    @param request:
    @param id: integer
    @return:
    """
    try:
        kot = Kot.objects.get(id=id)
    except Kot.DoesNotExist:
        raise Http404("Ce kot n'existe pas")
    return render(request, 'kot_location/kot_details.html', {'kot': kot})


def register_user(request):
    """
    Permits the registration from user using "UserCreationForm" from django auth library but modified in order to
    set up and use additional parameters
    @param request:
    @return:
    """
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = RegisterForm()
        if request.method == "POST":
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


def login_user(request):
    """
    Permits the authentification from the registered user using AuthentificationForm and login function from Django
    contrib auth libraries
    @param request:
    @return:
    """
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
    """
    Permits to logout an authentificated user with logout function from contrib auth django library
    @param request:
    @return:
    """
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")


@login_required(login_url='/login')
@permission_required('kot_location.add_kot', raise_exception=True)
def kot_add(request):
    """
    Permits to add a Kot when you're logged in and has the permission to add a Kot ad as a kot owner. If the user isn't
    logged, he is redirected to login page and if he isn't a owner, he doesn't have access to this page and gets
    403 code Forbidden
    @param request:
    @return:
    """
    if request.method == 'POST':
        form = KotForm(request.POST, request.FILES)
        if form.is_valid():
            start_date = form.cleaned_data.get("location_start_date")
            end_date = form.cleaned_data.get("location_end_date")
            days_number = end_date - start_date
            if end_date > start_date:
                kot = form.save(commit=False)
                kot.kot_owner_id = request.user.id
                kot.save()
                messages.add_message(request, messages.SUCCESS, 'Annonce en cours de validation.')
    else:
        form = KotForm()
    return render(request, 'kot_location/kot_add.html', {'form': form})


@login_required(login_url='/login')
def kot_delete(request, id: int):
    """
    Permits an kot owner to delete its kot ads available.
    @param request:
    @param id:
    @return:
    """
    kot_to_delete = Kot.objects.get(id=id)
    if request.user.id == kot_to_delete.kot_owner_id:
        kot_to_delete.delete()
        return redirect(f'/owner/{request.user.id}/offers')
    else:
        raise PermissionDenied


@login_required(login_url='/login')
def kot_update(request, id: int):
    """
    Permits an kot owner to update its kot ads available.
    @param request:
    @param id: int
    @return:
    """
    kot_to_update = Kot.objects.get(id=id)
    if request.user.id == kot_to_update.kot_owner_id:
        if request.method == 'POST':
            form = KotForm(request.POST, instance=kot_to_update)
            if form.is_valid():
                form.save()
                return redirect('kot-details', kot_to_update.id)
        else:
            form = KotForm(instance=kot_to_update)

        return render(request, 'kot_location/kot_update.html', {'kot': kot_to_update, 'form': form})
    else:
        raise PermissionDenied


@login_required(login_url='/login')
def kot_offers(request, id: int):
    """
    Permits to a user to consult its kot ads available
    @param request:
    @param id: int
    @return:
    @raise PermissionDenied: if you try to access to the offers from an other kot owner ID
    """
    if request.user.id == id:
        kots_from_owner = Kot.objects.filter(kot_owner_id=id)
        return render(request, 'kot_location/kot_owner_ads.html', {'kots': kots_from_owner})
    else:
        raise PermissionDenied


@login_required(login_url='/login')
@staff_member_required
def kot_validation_list(request):
    """
    Permits to a superuser to access to all the available ads awaiting validation
    @param request:
    @return:
    """
    all_kot_ad = KotAd.objects.all()
    kots = Kot.objects.all()

    return render(request, 'kot_location/kot_validation_list.html', {'kots': kots, 'kots_ads': all_kot_ad})


@login_required(login_url='/login')
@staff_member_required
def kot_check(request, id: int):
    """
    Pemits a superuser to validate a specific kot ad on validation page.
    @param request:
    @param id:
    @return:
    """
    kot_to_check = Kot.objects.get(id=id)
    KotAd.objects.create(kot_id=kot_to_check.id, is_active=True, publication_date=datetime.date.today())
    return redirect('/kot_list')


def renter_favorite_offers(request):
    return render(request, 'kot_location/client_favorite_offers.html')
