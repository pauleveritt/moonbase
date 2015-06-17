from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    ForeignKey,
)

from .sqltraversal import Node


class Folder(Node):
    __tablename__ = 'folder'
    id = Column(Integer, ForeignKey('node.id'), primary_key=True)
    title = Column(Text)
