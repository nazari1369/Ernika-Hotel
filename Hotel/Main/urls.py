from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_Page, name='Main_Page'),
]
