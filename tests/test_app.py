from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client_arranj):
    """
    Teste de 3 etapas [AAA]
    - A: Arrange  -> Arranjo/Organização
    - A: Act      -> Agir sobre a coisa
    - A: Assert   -> Afirmativa/Garantia que A é A
    - T: Teardown ->
    """

    # Arrange
    # client = TestClient(app)

    # Act
    response = client_arranj.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo!'}


def test_exercicio_2(client_arranj):
    # client = TestClient(app)

    response = client_arranj.get('/exercio_2_retorna_html')

    string_ola_mundo = response.text
    string_padrao = '<h1> Olá, Mundo!</h1>'

    assert response.status_code == HTTPStatus.OK
    assert string_padrao in string_ola_mundo


def test_create_user(client_arranj):
    # client = TestClient(app)

    response = client_arranj.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client_arranj):
    response = client_arranj.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'email': 'alice@example.com', 'username': 'alice'},
        ]
    }


def test_update_user_not_found(client_arranj):
    response = client_arranj.put(
        '/users/9999',
        json={
            'username': 'ghost',
            'email': 'ghost@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Deu ruim!! Não Achem emmm!!!'}


def test_update_user(client_arranj):
    response = client_arranj.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob_buxo@example.com',
            'password': 'segrect',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob_buxo@example.com',
        'id': 1,
    }
