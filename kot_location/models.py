from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    OWNER = 'OWNER'
    RENTER = 'RENTER'

    type_choice = {
        (OWNER, 'Propriétaire'),
        (RENTER, 'Locataire')
    }

    user_type = models.CharField(max_length=30, choices=type_choice)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday_date = models.DateField()
    is_tenant = models.BooleanField(default=False)


class KotOwner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday_date = models.DateField()


class Kot(models.Model):
    kot_address = models.CharField(max_length=256)
    price_month = models.DecimalField(max_digits=7, decimal_places=2)
    area_size = models.IntegerField()
    location_start_date = models.DateField(null=True)
    location_end_date = models.DateField(null=True)
    kot_owner = models.ForeignKey(KotOwner, on_delete=models.CASCADE)

    def is_valid_rent_date(self):
        return self.location_end_date > self.location_start_date


class KotAd(models.Model):
    publication_date = models.DateField()
    is_active = models.BooleanField(default=False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE)
