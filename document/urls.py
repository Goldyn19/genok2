from django.urls import path
from . import views
urlpatterns = [
    path('', views.documents, name='documents'),
    path('purchasebook', views.purchaseBook, name='purchasebook'),
    path('view_purchasebook', views.view_purchasebook, name='view_purchasebook'),
    path('newproduct', views.newProduct, name='newproduct'),
    path('credit', views.credit_record, name='credit_record' ),
    path('credit_detail/<str:credit_id>', views.credit_details, name='credit_detail')


]