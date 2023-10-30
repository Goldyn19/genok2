from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class ChatMessageForm(ModelForm):
    messageBody = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                               'style':'width: 800px; height:60px; background-color: #292929;color: white;',
                                                               "placeholder": "Type message Here"}))


    class Meta:
        model = ChatMessage
        fields = ['messageBody',]