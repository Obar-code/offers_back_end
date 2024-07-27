from django.contrib import admin
from .models import Account , Website , GlobalWebsite , Market
# Register your models here.

# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('email',)

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(GlobalWebsite)
class GlobalWebsiteAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(Market)
class Admin(admin.ModelAdmin):
    list_display = ('name_ar',)
