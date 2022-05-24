from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import UserStatus, Contracts, Country, JobTitle, Associates, Gender
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(UserStatus)
admin.site.register(Contracts)
admin.site.register(Country)
admin.site.register(JobTitle)
admin.site.register(Associates)
admin.site.register(Gender)