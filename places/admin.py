from django.contrib import admin
from .models import Country , Provinec , Directorate , AreWe , Advertising
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)
    

@admin.register(Provinec)
class ProvinecAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)


@admin.register(Directorate)
class DirectorateAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(AreWe)
class AreWeAdmin(admin.ModelAdmin):
    list_display = ('goal_ar',)

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)