from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

# Tabla "conoce_servicios_emergencia"
class ConoceServiciosEmergencia(models.Model):
    id_CSEmergencia = models.AutoField(primary_key=True)
    opcion_cse = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "conoce_numeros_emergencia"
class ConoceNumerosEmergencia(models.Model):
    id_CNEmergencia = models.AutoField(primary_key=True)
    opcion_cne = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "uso_911"
class Uso911(models.Model):
    id_Uso911 = models.AutoField(primary_key=True)
    opcion_uso911 = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "rapidez_servicio"
class RapidezServicio(models.Model):
    id_RServicio = models.AutoField(primary_key=True)
    opcion_rapidez = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "usar_app_emergencia"
class UsarAppEmergencia(models.Model):
    id_UApp = models.AutoField(primary_key=True)
    opcion_usarapp = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "avisos_recomendaciones"
class AvisosRecomendaciones(models.Model):
    id_AyR = models.AutoField(primary_key=True)
    opcion_avisos = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "mapa_interactivo"
class MapaInteractivo(models.Model):
    id_MapaInteractivo = models.AutoField(primary_key=True)
    opcion_mapa = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"

# Tabla "paleta_colores"
class PaletaColores(models.Model):
    id_PColores = models.AutoField(primary_key=True)
    opcion_paleta = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"
    
# Tabla "General"
class Formulario(models.Model):
    id_ResPersona = models.AutoField(primary_key=True)
    opcion_cse = models.CharField(max_length=255)
    opcion_cne = models.CharField(max_length=255)
    opcion_uso911 = models.CharField(max_length=255)
    opcion_rapidez = models.IntegerField()
    opcion_usarapp = models.CharField(max_length=255)
    opcion_avisos = models.CharField(max_length=255)
    opcion_mapa = models.CharField(max_length=255)
    opcion_paleta = models.CharField(max_length=255)

    def __str__(self):
        return f"Encuesta de servicios de emergencia: {self.pk}"


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=100, db_column='nombre_Usuario')
    correoUsuario = models.CharField(max_length=100, db_column='correo_Usuario')
    contraUsuario = models.CharField(max_length=128, db_column='contra_Usuario')
    last_login = models.DateTimeField(null=True, blank=True)

    def set_password(self, raw_password):
        self.contraUsuario = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contraUsuario)

    class Meta:
        db_table = 'UsuarioTabla'

class SupUsuario(models.Model):
    idSupUsuario = models.AutoField(primary_key=True)  # Autoincrementable
    nombreSupUsuario = models.CharField(max_length=100,db_column='nombre_SupUsuario')
    correoSupUsuario = models.CharField(max_length=100,db_column='correo_SupUsuario')
    contraSupUsuario = models.CharField(max_length=100,db_column='contra_SupUsuario')
    class Meta:
        db_table='SuperUsuarioTabla'