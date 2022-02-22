from django.contrib import admin

from .models import Kot, KotOwner

admin.site.register(Kot)
admin.site.register(KotOwner)