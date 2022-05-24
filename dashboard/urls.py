from django.urls import path
from dashboard import views
from .views import CountryGet, GenderGet, StatusGet



urlpatterns = [
    #path('create/', views.associates_post),
    path('country', CountryGet.as_view(), name='Country_List'),
    path('gender', GenderGet.as_view(), name='Gender_List'),
    path('status', StatusGet.as_view(), name='Status_List') 
]

