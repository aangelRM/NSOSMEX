from django.test import TestCase
from django.contrib.auth.hashers import make_password, check_password
from api.models import ConoceServiciosEmergencia, ConoceNumerosEmergencia, Uso911, RapidezServicio, UsarAppEmergencia, AvisosRecomendaciones, MapaInteractivo, PaletaColores, Formulario, Usuario, SupUsuario


class ModelTests(TestCase):
    def test_crear_instancia_conoce_servicios_emergencia(self):
        # Crea una instancia del modelo ConoceServiciosEmergencia y realiza pruebas
        servicio_emergencia = ConoceServiciosEmergencia(opcion_cse="Opción 1")
        self.assertEqual(servicio_emergencia.opcion_cse, "Opción 1")

    def test_crear_instancia_conoce_numeros_emergencia(self):
        # Crea una instancia del modelo ConoceNumerosEmergencia y realiza pruebas
        numeros_emergencia = ConoceNumerosEmergencia(opcion_cne="Opción 2")
        self.assertEqual(numeros_emergencia.opcion_cne, "Opción 2")

    def test_crear_instancia_uso_911(self):
        # Crea una instancia del modelo Uso911 y realiza pruebas
        uso_911 = Uso911(opcion_uso911="Opción 3")
        self.assertEqual(uso_911.opcion_uso911, "Opción 3")

    def test_crear_instancia_rapidez_servicio(self):
        # Crea una instancia del modelo RapidezServicio y realiza pruebas
        rapidez_servicio = RapidezServicio(opcion_rapidez="Opción 4")
        self.assertEqual(rapidez_servicio.opcion_rapidez, "Opción 4")

    def test_crear_instancia_usar_app_emergencia(self):
        # Crea una instancia del modelo UsarAppEmergencia y realiza pruebas
        usar_app_emergencia = UsarAppEmergencia(opcion_usarapp="Opción 5")
        self.assertEqual(usar_app_emergencia.opcion_usarapp, "Opción 5")

    def test_crear_instancia_avisos_recomendaciones(self):
        # Crea una instancia del modelo AvisosRecomendaciones y realiza pruebas
        avisos_recomendaciones = AvisosRecomendaciones(opcion_avisos="Opción 6")
        self.assertEqual(avisos_recomendaciones.opcion_avisos, "Opción 6")

    def test_crear_instancia_mapa_interactivo(self):
        # Crea una instancia del modelo MapaInteractivo y realiza pruebas
        mapa_interactivo = MapaInteractivo(opcion_mapa="Opción 7")
        self.assertEqual(mapa_interactivo.opcion_mapa, "Opción 7")

    def test_crear_instancia_paleta_colores(self):
        # Crea una instancia del modelo PaletaColores y realiza pruebas
        paleta_colores = PaletaColores(opcion_paleta="Opción 8")
        self.assertEqual(paleta_colores.opcion_paleta, "Opción 8")

    def test_crear_instancia_formulario(self):
        # Crea una instancia del modelo Formulario y realiza pruebas
        formulario = Formulario(
            opcion_cse="Opción 1",
            opcion_cne="Opción 2",
            opcion_uso911="Opción 3",
            opcion_rapidez=4,
            opcion_usarapp="Opción 5",
            opcion_avisos="Opción 6",
            opcion_mapa="Opción 7",
            opcion_paleta="Opción 8"
        )
        self.assertEqual(formulario.opcion_cse, "Opción 1")
        self.assertEqual(formulario.opcion_cne, "Opción 2")
        self.assertEqual(formulario.opcion_uso911, "Opción 3")
        self.assertEqual(formulario.opcion_rapidez, 4)
        self.assertEqual(formulario.opcion_usarapp, "Opción 5")
        self.assertEqual(formulario.opcion_avisos, "Opción 6")
        self.assertEqual(formulario.opcion_mapa, "Opción 7")
        self.assertEqual(formulario.opcion_paleta, "Opción 8")

    def test_crear_instancia_usuario(self):
        # Crea una instancia del modelo Usuario y realiza pruebas
        usuario = Usuario(nombreUsuario="Usuarios", correoUsuario="usuario@example.com", contraUsuario="contrasena123")
        self.assertEqual(usuario.nombreUsuario, "Usuarios")
        self.assertEqual(usuario.correoUsuario, "usuario@example.com")
        self.assertEqual(usuario.contraUsuario, "contrasena123")

    def test_set_password_and_check_password_usuario(self):
        # Crea una instancia del modelo Usuario y verifica el método set_password y check_password
        usuario = Usuario(nombreUsuario="usuario", correoUsuario="usuario@example.com", contraUsuario="contrasena123")
        usuario.save()

        usuario.set_password("nueva_contrasena")
        self.assertTrue(usuario.check_password("nueva_contrasena"))
        self.assertFalse(usuario.check_password("contrasena123"))

    def test_crear_instancia_sup_usuario(self):
        # Crea una instancia del modelo SupUsuario y realiza pruebas
        sup_usuario = SupUsuario(nombreSupUsuario="admin", correoSupUsuario="admin@example.com", contraSupUsuario="adminpass")
        self.assertEqual(sup_usuario.nombreSupUsuario, "admin")
        self.assertEqual(sup_usuario.correoSupUsuario, "admin@example.com")
        self.assertEqual(sup_usuario.contraSupUsuario, "adminpass")
