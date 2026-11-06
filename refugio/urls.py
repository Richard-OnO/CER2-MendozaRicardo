from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.lista_mascotas, name='catalogo'),
    path('mascota/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('gestion/', views.gestion_mascotas, name='gestion'),
]