from django.urls import path, include
from authentication import views
from .models import  Users
from .views import CustomUserView, Login
from rest_framework.routers import DefaultRouter


"""urlpatterns = [
    path('auth/register/', UsuarioView.as_view(), name='usuarios_list'),
    #path('tareas/eliminar/<id>',views.tareas_api)
    #path('my-data', MonitoringManager.as_view(), name= "monitoring_list"),
]"""

router = DefaultRouter()

router.register("user", CustomUserView)

urlpatterns = [   
path('login/',Login.as_view()),
path("", include(router.urls)),
]