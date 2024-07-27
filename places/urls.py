from django.urls import include , path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('country',views.Country)
router.register('provinec',views.Provinec)
router.register('directorate',views.Directorate)
router.register('arewe',views.AreWe)
router.register('advertising',views.Advertising)
urlpatterns = [
    path('',include(router.urls)),
]