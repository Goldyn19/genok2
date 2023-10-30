from django.urls import path
from . import views
urlpatterns = [
path('', views.fin_sec, name='fin_sec'),
]