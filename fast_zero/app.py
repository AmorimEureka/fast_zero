from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.get(
    '/exercio_2_retorna_html',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def exercicio_2_ola_mundo():
    return """
    <html>
        <head>
            <title> Nosso Ola Mundo!</Title>
        </head>
        <body>
            <h1> Olá, Mundo!</h1>
        </body>
    </html>"""
