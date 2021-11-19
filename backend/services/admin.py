from django.contrib import admin

# Register your models here.

from .models import Competences, Stacks, Experts, Tarifs, Services

admin.site.register(Competences)
admin.site.register(Stacks)
admin.site.register(Experts)
admin.site.register(Tarifs)
admin.site.register(Services)