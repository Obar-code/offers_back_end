from django.contrib import admin
from .models import CurrencyType , Coupon , Offer , LocalCoupon ,GlobalCoupon
# Register your models here.

@admin.register(CurrencyType)
class CurrencyTypeAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name_ar',)

@admin.register(LocalCoupon)
class LocalCouponAdmin(admin.ModelAdmin):
    list_display = ('description_ar',)

@admin.register(GlobalCoupon)
class GlobalCouponAdmin(admin.ModelAdmin):
    list_display = ('description_ar',)



