from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_and_compare, name='greet_and_compare'),
    path('advanced/', views.advanced_page, name='advanced_page'),
]