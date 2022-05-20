from django.urls import path
from dashboard import views
from .views import associates_post



urlpatterns = [
    path('create/', views.associates_post),   
]

