from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from django.contrib.auth import get_user_model


# Register your models here.
admin.site.register(Users, UserAdmin)
class Users(UserAdmin):
    pass

