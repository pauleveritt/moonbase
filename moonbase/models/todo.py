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
    dict(title='First ToDo'),
    dict(title='Change the air filters'),
    dict(title='Overdue Reminder'),
    dict(title='Get the milk')
]
