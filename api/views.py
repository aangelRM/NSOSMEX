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

""
# apis
import googlemaps
import requests

def tu_vista(request):
    api_key = settings.GOOGLE_MAPS_API_KEY
    return render(request, 'mapa.html', {'api_key': api_key})

def vista_tiempo(request):
    return render(request, 'clima.html')

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
        return render(request, 'terremotos.html', {'terremotos': terremotos})
    else:
        return render(request, 'terremotos.html', {'terremotos': []})  # Maneja el caso de error










class Login(View):
    template_name = "login.html"

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



    
class Forgot_password(APIView):
    template_name = "pages/examples/forgot-password.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Register(APIView):
    template_name = "pages/examples/register.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Recover_password(APIView):
    template_name = "pages/examples/recover-password.html"
    def post(self, request):
        return render(request, self.template_name)

class FormularioUsuarioView(HttpRequest):

    def index(request):
        Usuario = UsuarioForm()
        return render(request, 'pages/examples/register.html', {"form": Usuario})

    def procesar_formulario(request):
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                # Obtener los datos del formulario
                correo = form.cleaned_data['correoUsuario']
                password = form.cleaned_data['contraUsuario']

                # Crear un usuario con la contraseña cifrada
                user = Usuario(correoUsuario=correo)
                user.set_password(password)
                user.save()

                # Crear el mensaje del correo electrónico
                subject = 'Bienvenida'
                from_email = 'angel585244102@gmail.com'  # Reemplaza con tu dirección de correo
                recipient_list = [correo]
                message = render_to_string('correo.html', {'user': user})

                # Enviar el correo electrónico
                try:
                    send_mail(subject, message, from_email, recipient_list)
                except SMTPException:
                    print('Error al enviar el correo electrónico')

                return render(request, "pages/examples/register.html", {"form": UsuarioForm(), "mensaje": "OK"})

        # Si llegamos aquí, hubo un error en el formulario
        return render(request, "pages/examples/register.html", {"form": UsuarioForm(), "error_message": "Error en el formulario"})

            
        
        
        
class Main(APIView):
    template_name = "index.html"
    def get(self, request):
        context={
            
        }
        return render(request, self.template_name)
    
class Home1(APIView):
    template_name = "index.html"
    def post(self, request):
        return render(request, self.template_name)

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

