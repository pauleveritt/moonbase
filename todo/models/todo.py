from sqlalchemy.schema import Column
from sqlalchemy.types import (
    Integer,
    Text,
)
from pyramid_sqlalchemy import BaseObject

class ToDoItem(BaseObject):
    __tablename__ = 'todoitem'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
