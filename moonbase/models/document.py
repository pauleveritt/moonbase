from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)

from .sqltraversal import Node


class Document(Node):
    __tablename__ = 'document'
    id = Column(Integer, ForeignKey('node.id'), primary_key=True)
    title = Column(Text)
