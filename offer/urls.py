from django.urls import include , path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('currency',views.CurrencyType)
router.register('offers',views.Offer)
router.register('coupons',views.Coupon)
router.register('localcoupon',views.LocalCoupon)
router.register('globalcoupon',views.GlobalCoupon)
urlpatterns = [
    path('',include(router.urls)),
]