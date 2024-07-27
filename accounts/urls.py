from django.urls import path , include
from rest_framework import routers
from . import views
from .views import AccountCreateView

router = routers.DefaultRouter()
router.register('webs',views.Website)
router.register('markets',views.Market)
router.register('globalwebsite',views.GlobalWebsite)
urlpatterns = [
    path('',include(router.urls)),
    path('register/', AccountCreateView.as_view(), name='user-create'),
    # path('login/',CustomLoginView.as_view(),name='user-lgoin'),
    # path('chang_password/',ChangePasswordView.as_view(),name='user-chang-password'),
    # path('delete_user/',DeleteUserView.as_view(),name='delete-user'),
]