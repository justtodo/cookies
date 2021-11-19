from django.contrib import admin

# Register your models here.

from .models import Pack, Premium

admin.site.register(Pack)
admin.site.register(Premium)