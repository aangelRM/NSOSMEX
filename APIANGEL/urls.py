from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from api.views import *
from api import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('forgot-password/', Forgot_password.as_view(), name='forgot_password'),
    path('recover-password/', Recover_password.as_view(), name='recover_password'),
    path('index/', Main.as_view(), name='main'),
    path('index/', Home1.as_view(), name='home1'),
    path('index2/', Home2.as_view(), name='home2'),
    path('index3/', Home3.as_view(), name='home3'),
    path('widgets/', Widgets.as_view(), name='widgets'),
    path('registarUsuario/', FormularioUsuarioView.index, name="registarUsuario"),
    path('guardarUsuario/', FormularioUsuarioView.procesar_formulario, name="guardarUsuario"),
    path('clima/', views.vista_tiempo, name='vista_tiempo'),
    path('terremotos/', views.vista_terremotos, name='terremotos'),
    path('mapa/', views.tu_vista, name='vista_mapa'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
