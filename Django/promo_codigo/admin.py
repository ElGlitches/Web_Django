from django.contrib import admin
from .models import PromoCodigo

class CodigoPromoAdmin(admin.ModelAdmin):
    exclude = ['codigo']

# Register your models here.
admin.site.register(PromoCodigo,CodigoPromoAdmin)
