from data import db_session
from data.users import User


def create_user():
    user = User(
        word=None,
        attempts=0
    )
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

