import pytest
from api.models import ConoceServiciosEmergencia, ConoceNumerosEmergencia, Uso911, RapidezServicio, UsarAppEmergencia, AvisosRecomendaciones, MapaInteractivo, PaletaColores, Formulario, Usuario, SupUsuario

@pytest.fixture
def crear_instancia_usuario():
    return Usuario.objects.create_user(
        nombreUsuario="Usuarios",
        correoUsuario="usuario@example.com",
        contraUsuario="contrasena123"
    )

def test_crear_instancia_conoce_servicios_emergencia():
    servicio_emergencia = ConoceServiciosEmergencia(opcion_cse="Opción 1")
    assert servicio_emergencia.opcion_cse == "Opción 1"

def test_crear_instancia_conoce_numeros_emergencia():
    numeros_emergencia = ConoceNumerosEmergencia(opcion_cne="Opción 2")
    assert numeros_emergencia.opcion_cne == "Opción 2"

def test_crear_instancia_uso_911():
    uso_911 = Uso911(opcion_uso911="Opción 3")
    assert uso_911.opcion_uso911 == "Opción 3"

def test_crear_instancia_rapidez_servicio():
    rapidez_servicio = RapidezServicio(opcion_rapidez="Opción 4")
    assert rapidez_servicio.opcion_rapidez == "Opción 4"

def test_crear_instancia_usar_app_emergencia():
    usar_app_emergencia = UsarAppEmergencia(opcion_usarapp="Opción 5")
    assert usar_app_emergencia.opcion_usarapp == "Opción 5"

def test_crear_instancia_avisos_recomendaciones():
    avisos_recomendaciones = AvisosRecomendaciones(opcion_avisos="Opción 6")
    assert avisos_recomendaciones.opcion_avisos == "Opción 6"

def test_crear_instancia_mapa_interactivo():
    mapa_interactivo = MapaInteractivo(opcion_mapa="Opción 7")
    assert mapa_interactivo.opcion_mapa == "Opción 7"

def test_crear_instancia_paleta_colores():
    paleta_colores = PaletaColores(opcion_paleta="Opción 8")
    assert paleta_colores.opcion_paleta == "Opción 8"

def test_crear_instancia_formulario():
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
    assert formulario.opcion_cse == "Opción 1"
    assert formulario.opcion_cne == "Opción 2"
    assert formulario.opcion_uso911 == "Opción 3"
    assert formulario.opcion_rapidez == 4
    assert formulario.opcion_usarapp == "Opción 5"
    assert formulario.opcion_avisos == "Opción 6"
    assert formulario.opcion_mapa == "Opción 7"
    assert formulario.opcion_paleta == "Opción 8"

def test_crear_instancia_usuario(crear_instancia_usuario):
    instancia = crear_instancia_usuario
    assert instancia.nombreUsuario == "Usuarios"
    assert instancia.correoUsuario == "usuario@example.com"
    assert instancia.contraUsuario == "contrasena123"

def test_set_password_and_check_password_usuario(crear_instancia_usuario):
    usuario = crear_instancia_usuario
    usuario.set_password("nueva_contrasena")
    assert usuario.check_password("nueva_contrasena")
    assert not usuario.check_password("contrasena123")

def test_crear_instancia_sup_usuario():
    sup_usuario = SupUsuario(nombreSupUsuario="admin", correoSupUsuario="admin@example.com", contraSupUsuario="adminpass")
    assert sup_usuario.nombreSupUsuario == "admin"
    assert sup_usuario.correoSupUsuario == "admin@example.com"
    assert sup_usuario.contraSupUsuario == "adminpass"
