from django.contrib import admin

# Register your models here.

from .models import Premium, Packs

admin.site.register(Premium)
admin.site.register(Packs)