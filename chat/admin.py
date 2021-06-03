from django.contrib import admin
from .models import Room, Message

# Регистрация таблиц
admin.site.register(Room)
admin.site.register(Message)