from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import View
from django.conf import settings
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse , HttpRequest
from .forms import UsuarioForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from smtplib import SMTPException
from django.utils.crypto import get_random_string
from django.contrib import messages

import random
from django.contrib.auth.hashers import make_password


#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#------------------------------------------------- apis ------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

import googlemaps
import requests

def tu_vista(request):
    api_key = settings.GOOGLE_MAPS_API_KEY
    return render(request, 'pages/template_apis/mapa.html', {'api_key': api_key})

def vista_tiempo(request):
    return render(request, 'pages/template_apis/clima.html')

# En views.py
def obtener_terremotos_mexico():
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    parametros = {
        'format': 'geojson',
        'starttime': '2023-01-01',
        'minmagnitude': 5.0,
        'maxlatitude': 32.718,
        'minlatitude': 14.532,
        'maxlongitude': -86.593,
        'minlongitude': -118.276,
        'limit': 10
    }

    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code == 200:
        datos_terremotos = respuesta.json()
        return datos_terremotos['features']  # Devolver solo la lista de terremotos
    else:
        print(f"Error al obtener datos. Código de estado: {respuesta.status_code}")
        return None

def vista_terremotos(request):
    terremotos = obtener_terremotos_mexico()

    if terremotos is not None:
        return render(request, 'pages/template_apis/terremotos.html', {'terremotos': terremotos})
    else:
        return render(request, 'pages/template_apis/terremotos.html', {'terremotos': []})  # Maneja el caso de error




#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#------------------------------------------------- login -----------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#


class Login(View):
    template_name = "pages/registration/login.html"

    def get(self, request):
        form = UsuarioForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UsuarioForm(data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('correoUsuario')
            password = form.cleaned_data.get('contraUsuario')

            # Autenticar al usuario
            user = authenticate(request, correoUsuario=correo, contraUsuario=password)
            print(f'Usuario: {user}, Correo: {correo}, Contraseña: {password}')

            if user is not None:
                # Usuario autenticado, iniciar sesión
                login(request, user)
                print('Usuario autenticado')
                return redirect('home2')

        print('Credenciales inválidas')
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UsuarioForm(data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('correoUsuario')
            password = form.cleaned_data.get('contraUsuario')
            print(f'Credenciales: Correo: {correo}, Contraseña: {password}')

            try:
                user = Usuario.objects.get(correoUsuario=correo)
                if check_password(password, user.contraUsuario):
                    print(f'Usuario autenticado: {user}')
                    login(request, user)
                    return redirect('home2')
                else:
                    print('Contraseña incorrecta')
            except Usuario.DoesNotExist:
                print('Usuario no encontrado')
        else:
            print("Formulario no válido. Errores:", form.errors)

        return render(request, self.template_name, {'form': form})

#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------- Recuperar contraseña -----------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

    




class Forgot_password(View):
    template_name = "pages/registration/forgot-password-v2.html"

    def get(self, request):
        form = UsuarioForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UsuarioForm(request.POST)

        if form.is_valid():
            # Obtener los datos del formulario
            correo = form.cleaned_data['correoUsuario']

            # Verificar si el correo existe en la base de datos
            if Usuario.objects.filter(correoUsuario=correo).exists():
                # Redirigir a la página de recuperación de contraseña
                return redirect('recover_password', correo=correo)
            else:
                # Mostrar un mensaje si el correo no está registrado
                error_message = "No hay ningún correo registrado con esa dirección."
                return render(request, self.template_name, {"form": UsuarioForm(), "error_message": error_message})

        # Si el formulario no es válido, vuelve a mostrar la página de recuperación
        return render(request, self.template_name, {"form": form})









class Recover_password(View):
    template_name = "pages/registration/recover-password-v2.html"

    def get(self, request, correo):
        return render(request, self.template_name, {'correo': correo})

    def post(self, request, correo):
        # Obtener el correo directamente de los datos POST
        correo = request.POST.get('correoUsuario')

        codigo_ingresado = request.POST.get('codigo')
        nueva_contrasena = request.POST.get('nueva_contrasena')

        try:
            usuario = Usuario.objects.get(correoUsuario=correo, codigo_recuperacion=codigo_ingresado)
        except Usuario.DoesNotExist:
            messages.error(request, 'El código ingresado no es válido. Intenta de nuevo.')
            return render(request, self.template_name, {'correo': correo})

        # Si el código es válido, actualiza la contraseña y limpia el código
        usuario.contraUsuario = nueva_contrasena
        usuario.codigo_recuperacion = None  # Limpia el código de recuperación
        usuario.save()

        messages.success(request, 'Contraseña cambiada exitosamente. Ahora puedes iniciar sesión con tu nueva contraseña.')

        return redirect('login')  # O redirige a donde desees después del cambio de contraseña


       


class IngresarCodigo(View):
    template_name = "pages/examples/ingresar-codigo.html"

    def get(self, request, correo):
        return render(request, self.template_name, {'correo': correo})

    def post(self, request, correo):
        codigo = request.POST.get('codigo')
        nueva_contrasena = request.POST.get('nueva_contrasena')

        try:
            usuario = Usuario.objects.get(correoUsuario=correo, codigo_recuperacion=codigo)
            
            # Validar el código (puedes agregar más lógica según tus necesidades)

            # Actualizar la contraseña
            usuario.contraUsuario = make_password(nueva_contrasena)
            usuario.codigo_recuperacion = None  # Limpiar el código de recuperación
            usuario.save()

            messages.success(request, 'Contraseña actualizada correctamente. Puedes iniciar sesión con la nueva contraseña.')
            return redirect('login')  # Puedes redirigir a donde desees después de la actualización

        except Usuario.DoesNotExist:
            messages.error(request, 'Código de recuperación no válido. Intenta de nuevo o solicita un nuevo código.')
            return redirect('ingresar_codigo', correo=correo)



#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#--------------------------------------------- Registro ------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

    
class Register(APIView):
    template_name = "pages/registration/register.html"
    def get(self, request):
        return render(request, self.template_name)

class FormularioUsuarioView(View):
    def index(request):
        Usuario = UsuarioForm()
        return render(request, 'pages/registration/register.html', {"form": Usuario})

    def procesar_formulario(request):
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                # Obtener los datos del formulario
                nombre_usuario = form.cleaned_data.get('nombreUsuario', '')
                correo = form.cleaned_data['correoUsuario']
                password = form.cleaned_data['contraUsuario']
                
                if Usuario.objects.filter(correoUsuario=correo).exists():
                    return render(request, "pages/registration/register.html", {"form": UsuarioForm(), "error_message": "El correo ya está registrado"})

                # Crear un usuario con la contraseña cifrada
                user = Usuario(correoUsuario=correo, nombreUsuario=nombre_usuario)
                user.set_password(password)
                user.save()
                
                login(request, user)

                # Crear el mensaje del correo electrónico
                subject = 'Bienvenida'
                from_email = 'angel585244102@gmail.com'
                recipient_list = [correo]

                # Renderizar la plantilla como una cadena HTML
                html_message = render_to_string('pages/registration/correo.html', {'user': user, 'nombre_usuario': nombre_usuario})


                # Enviar el correo electrónico
                try:
                    send_mail(subject, '', from_email, recipient_list, html_message=html_message)
                except SMTPException:
                    print('Error al enviar el correo electrónico')
                
                return redirect('login')
        # Si llegamos aquí, hubo un error en el formulario
        return render(request, "pages/registration/register.html", {"form": UsuarioForm(), "error_message": "Error en el formulario"})
            


#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------------- Otras vistas -------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#


class Main(APIView):
    template_name = "index.html"

    def get(self, request):
        context = {'user': request.user}
        print(request.user)  # Agrega esta línea para imprimir información de usuario en la consola
        return render(request, self.template_name, context)

    
class Home1(APIView):
    template_name = "index.html"

    def get(self, request):
        context = {'user': request.user}
        return render(request, self.template_name, context)


class Home2(APIView):
    template_name = "index2.html"
    def get(self, request):
            return render(request, self.template_name)
    
class Home3(APIView):
    template_name = "index3.html"
    def get(self, request):
        return render(request, self.template_name)
    

class Widgets(APIView):
    template_name = "pages/widgets.html"
    def get(self, request):
        return render(request, self.template_name)







#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#---------------------------------- Limpiar base de produccion -----------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#


def eliminar_todos_los_usuarios(request):
    # Obtén la QuerySet de todos los usuarios y elimínalos
    Usuario.objects.all().delete()

    # Redirige a la página deseada después de la eliminación
    return redirect('login')



def ver_todos_los_registros(request):
    # Obtén la QuerySet de todos los registros
    registros = Usuario.objects.all()

    # Pasa la QuerySet a la plantilla para mostrar los registros
    return render(request, 'mapa.html', {'registros': registros})
