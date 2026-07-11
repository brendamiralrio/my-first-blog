#Brenda Marquez
#07/10/2026
#Django URLS

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]