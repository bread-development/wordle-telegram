import sqlalchemy

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    word = sqlalchemy.Column(sqlalchemy.String)
    attempts = sqlalchemy.Column(sqlalchemy.Integer)
