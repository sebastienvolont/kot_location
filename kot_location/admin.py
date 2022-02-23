from django.contrib import admin

from .models import Kot, KotOwner, User

admin.site.register(Kot)
admin.site.register(KotOwner)
admin.site.register(User)