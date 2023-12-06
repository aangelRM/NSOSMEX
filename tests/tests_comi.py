import pytest
from api.models import Usuario

@pytest.mark.django_db
def test_crear_usuario():
    user = Usuario.objects.create_user(
        nombreUsuario='angel',
        correoUsuario='usuario@example.com',
        contraUsuario='contrasena123',
    )

    assert user.nombreUsuario == 'angel'

