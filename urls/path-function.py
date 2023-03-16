from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome/', views.home, name='my-welcome')
]