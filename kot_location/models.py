from django.db import models


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
    location_start_date = models.DateField()
    location_end_date = models.DateField()
    kot_owner = models.ForeignKey(KotOwner, on_delete=models.CASCADE)


class KotAd(models.Model):
    publication_date = models.DateField()
    is_active = models.BooleanField(default=False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE)
