from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_mundo_deve_retornar_um_html():
    client = TestClient(app)

    response = client.get('/ola_mundo')

    assert '<h1> Olá Mundo </h1>' in response.text
