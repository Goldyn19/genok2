from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, Profile
from .forms import ChatMessageForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


def Chat(request):
    user = request.user.id
    profile = Profile.objects.all
    template = loader.get_template('chat.html')
    context = {
        'profile': profile,
        "user": user,
    }
    return HttpResponse(template.render(context, request))


def ChatDetails(request, pk):
    user_id = request.user.id
    pk = pk
    profile = Profile.objects.all()
    #receiver_profile = Profile.objects.get(id=pk)
    receiver_profile = get_object_or_404(Profile, id=pk)
    sender_profile = get_object_or_404(Profile, user=user_id)
    chat = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(sender=sender_profile, receiver=receiver_profile, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = sender_profile
            chat_message.receiver = receiver_profile
            chat_message.save()
            return redirect('chat_details', receiver_profile.id)
    template = loader.get_template('chat-details.html')
    context = {
        "form": form,
        "chat": chat,
        "sender_profile": sender_profile,
        'profile': profile,
        'receiver_profile': receiver_profile,
        'num': rec_chats.count()

    }
    return HttpResponse(template.render(context, request))




def remove_chat(request):
    item1 = ChatMessage.objects.all()
    item1.delete()

# Create your views here.


# Create your views here.
