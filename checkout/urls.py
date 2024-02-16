from django.urls import path
from . import views
urlpatterns = [
    path('', views.fin_sec, name='fin_sec'),
    path('confirm/<str:cart_id>', views.confirm_checkout, name='confirm_checkout')
]