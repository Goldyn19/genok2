from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.Carts, name='carts'),
    path('view_cart/<str:cart_id>', views.Create_cart, name='create_cart'),
    path('view_cart/<str:cart_id>/add_to_cart/<str:part_number>/<int:quantity>', views.Add_To_Cart, name='add_to_cart'),
    path('view_cart/view_details/<str:cart_id>', views.View_cart_details, name='view_cart_details'),
    path('checkout/<str:cart_id>', views.checkout, name='checkout'),
    path('proceed_to_payement/<str:cart_id>', views.proceed_payment, name='proceed_to_payment')

]