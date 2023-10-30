from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User

def index(request):
    username = request.user.username
    template = loader.get_template('index.html')
    context = {
        'username': username
    }
    return HttpResponse(template.render(context, request))

def alert(request):
    user = request.user.username
    user_id = get_object_or_404(User, username=user)
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "fin_sec":
        return redirect('patient_vitals', user_id.id)
    elif group.name == "sec":
        return redirect('view_patients')
    else:
        return  redirect('dashboard')
# Create your views here.
