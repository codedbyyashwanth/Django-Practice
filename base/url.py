from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home, name="Home"),
        path('store/<str:id>', views.App, name="store"),
]