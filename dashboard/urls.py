from django.urls import path
from dashboard import views
from .views import CountryGet, SexGet, StatusGet



urlpatterns = [
    #path('create/', views.associates_post),
    path('country', CountryGet.as_view(), name='Country_List'),
    path('sex', SexGet.as_view(), name='Sex_List'),
    path('status', StatusGet.as_view(), name='Status_List') 
]

