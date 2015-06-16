import colander
from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import BaseObject


class ToDoItemSchema(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())


class ToDoItem(BaseObject):
    __tablename__ = 'todoitem'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
