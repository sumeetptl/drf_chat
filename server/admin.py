from django.contrib import admin

# Register your models here.
from .models import Category, Channel, Server

# Register your models here.
admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Server)
