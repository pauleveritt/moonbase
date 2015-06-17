from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import BaseObject


class ToDo(BaseObject):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)

TODOS = [
    dict(
        id=1,
        title='First ToDo'
    ),
    dict(
        id=2,
        title='Change the air filters'
    ),
    dict(
        id=3,
        title='Overdue Reminder'
    ),
    dict(
        id=4,
        title='Get the milk'
    )
]
