from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI(title='Projeto Amoras')

database = []


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


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    # Acoplamento de codigo externo
    # Impossibilita a testagem externa antes do teste do endpoint
    # session = get_session()

    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Username already exists',
            )
        elif db_user == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, detail='Email already exists'
            )

    db_user = User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

    # breakpoint()
    # return user
    # user_with_id = UserDB(
    #     **user.model_dump(),
    #     # username=user.username,
    #     # email=user.email,
    #     # password=user.password,
    #     id=len(database) + 1,
    # )

    # database.append(user_with_id)

    # return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).limit(limit).offset(offset))
    return {'users': users}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):

    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    user_db.email = user.email
    user_db.username = user.username
    user_db.password = user.password

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db

    # user_with_id = UserDB(**user.model_dump(), id=user_id)

    # if user_id < 1 or user_id > len(database):
    #     raise HTTPException(
    #         status_code=HTTPStatus.NOT_FOUND,
    #         detail='Deu ruim!! Não Achem emmm!!!',
    #     )

    # database[user_id - 1] = user_with_id

    # return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=Message
)
def delete_user(
    user_id: int, session: Session = Depends(get_session)
):

    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    session.delete(user_db)
    session.commit()

    # return {'message': 'user deleted'}
    return Message(message='user deleted')

    # if user_id > len(database) or user_id < 1:
    #     raise HTTPException(
    #         status_code=HTTPStatus.NOT_FOUND, detail='user not found'
    #     )

    # del database[user_id - 1]

    # return {'message': 'user deleted'}
