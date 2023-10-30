from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Chat, name='chats'),
    path("<int:pk>", views.ChatDetails, name='chat_details')
]
