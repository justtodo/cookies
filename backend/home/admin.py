from django.contrib import admin

# Register your models here.

from .models import Premium, Pack

admin.site.register(Premium)
admin.site.register(Pack)