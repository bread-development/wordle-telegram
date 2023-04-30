from data import db_session
from data.users import User


def change_word(id_, word):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id_).first()
    user.word = word
    db_sess.commit()


def change_attempts(id_, attempts):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id_).first()
    user.attempts = attempts
    db_sess.commit()


def change_status(id_, in_game):
    # устанавливаем, идет игра или нет
    pass
