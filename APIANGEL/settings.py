import os
from pathlib import Path
import environ
import dj_database_url


env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    'api',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'APIANGEL.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

WSGI_APPLICATION = 'APIANGEL.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'postgres://nsosbd_user:WVO5wM6oxnDiNyLY9CdRjTTOvrrCz4bl@dpg-clfqsdug1b2c73a3hshg-a/nsosbd',
#         'PORT': 5432,
#         'NAME': 'nsosbd',
#         'USER': 'nsosbd_user',
#         'PASSWORD': 'WVO5wM6oxnDiNyLY9CdRjTTOvrrCz4bl',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

    
}



# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'






# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py

# Configuración de correo electrónico
EMAIL_USE_TLS = True  # Usar TLS para conexión segura
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP de Gmail     
EMAIL_PORT = 587  # Puerto de Gmail para TLS/STARTTLS 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Credenciales de correo electrónico de Gmail
EMAIL_HOST_USER = 'angel585244102@gmail.com'  # Tu dirección de correo de Gmail
EMAIL_HOST_PASSWORD = 'jgfmvwqfyqgvnexu'  # Contraseña de tu cuenta de Gmail

# Configuración adicional para Gmail
# DEFAULT_FROM_EMAIL = 'angel585244102@gmail.com'  # Dirección predeterminada para enviar correos
# Asegúrate de habilitar "Acceso de aplicaciones menos seguras" en tu cuenta de Gmail
# Si deseas usar OAuth 2.0 para autenticación, hay que configurarla de forma diferente
