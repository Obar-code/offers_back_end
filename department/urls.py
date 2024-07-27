from django.urls import include , path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('departments',views.Department)
urlpatterns = [
    path('',include(router.urls)),
]