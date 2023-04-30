from data import db_session
from data.users import User


def req_user(id_):
    #чекаем, есть ли юзер в базе
    pass


def req_word(id_):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id_).first()
    return user.word


def req_attempts(id_):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id_).first()
    return user.attempts

def req_status(id_):
    # здесь чекаем, есть незаконченная игра или нет, если есть, то return True, иначе False
    pass