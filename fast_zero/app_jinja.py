from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = Path(__file__).parent

# diretorio que contem o arquivo estatico
# '.mount()' criar endpoint '/static'
app.mount(
    '/static', StaticFiles(directory=str(BASE_DIR / 'static')), name='static'
)

# Mapeia o diretorio contendo os arquivos estaticos
templates = Jinja2Templates(directory=str(BASE_DIR / 'templates'))


# O objeto Request é o objeto c/ o corpo da requisição e seu escopo.
# O método TemplateResponse diz:
#   - objeto com corpo da requisoção
#   - nome do template que será renderizado
#   - context é o dicionário que passa as variáveis do endpoint,
#     isto é, o valor passado em '/{texto_url}' para o arquivo html.
@app.get('/{texto_url}', response_class=HTMLResponse)
def home(request: Request, texto_url: str):
    return templates.TemplateResponse(
        request=request, name='index.html', context={'nome': texto_url}
    )
