from django.contrib import admin

from .models import Profile, ChatMessage


admin.site.register([Profile, ChatMessage])

# Register your models here.
