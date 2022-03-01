from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    OWNER = 'OWNER'
    RENTER = 'RENTER'
    ADMINISTRATOR = 'ADMIN'

    type_choice = {
        (OWNER, 'Propriétaire'),
        (RENTER, 'Locataire')
    }

    user_type = models.CharField(max_length=30, choices=type_choice)


class Kot(models.Model):
    Brussels = 'Bruxelles'
    Louvain_La_Neuve = 'Louvain-la-Neuve'
    Liege = 'Liège'
    Namur = 'Namur'

    city_choice = {
        (Brussels, 'Bruxelles'),
        (Louvain_La_Neuve, 'Louvain-la-Neuve'),
        (Liege, 'Liège'),
        (Namur, 'Namur')
    }

    kot_address = models.CharField(max_length=256)
    kot_city = models.CharField(max_length=30, choices=city_choice)
    kot_image = models.ImageField(upload_to='kot_location/',
                                  default="https://d34ip4tojxno3w.cloudfront.net/app/uploads/placeholder.jpg")
    price_month = models.DecimalField(max_digits=7, decimal_places=2)
    area_size = models.IntegerField()
    location_start_date = models.DateField(null=True)
    location_end_date = models.DateField(null=True)
    kot_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_valid_rent_date(self):
        return self.location_end_date > self.location_start_date


class KotAd(models.Model):
    publication_date = models.DateField()
    is_active = models.BooleanField(default=False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE)


class RenterFavoriteAd(models.Model):
    renter_user = models.ForeignKey(Kot, on_delete=models.CASCADE)
    followed_ad = models.ForeignKey(KotAd, on_delete=models.CASCADE)
