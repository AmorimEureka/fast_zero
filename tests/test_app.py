from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Teste de 3 etapas [AAA]
    - A: Arrange  -> Arranjo/Organização
    - A: Act      -> Agir sobre a coisa
    - A: Assert   -> Afirmativa/Garantia que A é A
    - T: Teardown ->
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo!'}
