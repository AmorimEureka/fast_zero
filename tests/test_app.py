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


def test_exercicio_2():
    client = TestClient(app)

    response = client.get('/exercio_2_retorna_html')

    string_ola_mundo = response.text
    string_padrao = '<h1> Olá, Mundo!</h1>'

    assert response.status_code == HTTPStatus.OK
    assert string_padrao in string_ola_mundo
