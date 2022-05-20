from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import StatusUser, Contrato, Country, JobTitle, Colleagues
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(StatusUser)
admin.site.register(Contrato)
admin.site.register(Country)
admin.site.register(JobTitle)
admin.site.register(Colleagues)