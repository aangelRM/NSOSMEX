from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from api.views import *
from django.urls import path, reverse_lazy
from api import views

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('Registro/', Register.as_view(), name='register'),
    # path('Olvidaste-tu-contraseña/', Forgot_password.as_view(), name='forgot_password'),
    # path('Cambiar-contraseña/', Recover_password.as_view(), name='recover_password'),

    path('index/', Main.as_view(), name='main'),
    path('home1/', Home1.as_view(), name='home1'),
    path('registarUsuario/', FormularioUsuarioView.index, name="registarUsuario"),
    path('guardarUsuario/', FormularioUsuarioView.procesar_formulario, name="guardarUsuario"),
    path('logout/', logout_view, name='logout'),
    path('clima/', views.vista_tiempo, name='vista_tiempo'),
    path('terremotos/', views.vista_terremotos, name='terremotos'),
    path('mapa/', views.tu_vista, name='vista_mapa'),
    # path('ver_todos_los_registros/', views.ver_todos_los_registros, name='ver_todos_los_registros'),
    path('eliminar_todos_los_usuarios/', views.eliminar_todos_los_usuarios, name='eliminar_todos_los_usuarios'),
]

