from django.test import TestCase
from .models import Kot


class KotModelTests(TestCase):
    def test_kot_invalid_date_published_in_past(self):
        past_ad_kot = Kot(kot_address="test1", price_month=550, area_size=45, location_start_date="2022-08-02",
                          location_end_date="2022-07-05", kot_owner_id=1)
        self.assertIs(past_ad_kot.is_valid_rent_date(), False)

    def test_kot_valid_date(self):
        past_ad_kot = Kot(kot_address="test2", price_month=550, area_size=45, location_start_date="2022-08-02",
                          location_end_date="2022-12-05", kot_owner_id=1)
        self.assertIs(past_ad_kot.is_valid_rent_date(), False)
