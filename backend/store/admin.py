from django.contrib import admin

# Register your models here.

from .models import Produit, Images

admin.site.register(Produit)
admin.site.register(Images)