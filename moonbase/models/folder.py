from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)

from .node import Node


class Folder(Node):
    __tablename__ = 'folder'
    id = Column(Integer, ForeignKey('node.id'), primary_key=True)
    title = Column(Text)

class RootFolder(Folder):
    pass