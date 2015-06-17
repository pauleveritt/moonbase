from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey,
    String
)
from sqlalchemy.orm import (
    relationship,
    backref
)
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.util import classproperty
from sqlalchemy.dialects.postgresql import JSONB

from pyramid_sqlalchemy import BaseObject, Session

def root_factory(request):
    return Session.query(Node).filter_by(parent_id=None).one()


class Node(BaseObject):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), nullable=False)
    parent_id = Column(Integer, ForeignKey('node.id'))
    children = relationship("Node",
                            backref=backref('parent', remote_side=[id])
    )
    type = Column(String(50))
    __acl__ = Column(JSONB)

    @classproperty
    def __mapper_args__(cls):
        return dict(
            polymorphic_on='type',
            polymorphic_identity=cls.__name__.lower(),
            with_polymorphic='*',
        )

    def __setitem__(self, key, node):
        node.name = str(key)
        if self.id is None:
            Session.flush()
        node.parent_id = self.id
        Session.add(node)
        Session.flush()

    def __getitem__(self, key):
        try:
            return Session.query(Node).filter_by(
                name=key, parent=self).one()
        except NoResultFound:
            raise KeyError(key)

    def values(self):
        return Session.query(Node).filter_by(parent=self)

    @property
    def __name__(self):
        return self.name

    @property
    def __parent__(self):
        return self.parent

    # TODO This would be better as something not in Python, but
    # instead, something that could run in the query, perhaps
    # effectively using the optimizer, perhaps done well in
    # SQLAlchemy. It would be nice to optimized even further by bailing
    # out as soon as a node (context or a parent) had a Deny that
    # failed. Finally, perhaps we have to, like Substance D, maintain
    # some other datastructure.


    # This is fast in Substance D because most things are not in the
    # ObjectMap's path_to_acl, as they have the default acl of none.
    def allowed_values(self, principals, permission):
        results = []
        for child in self.values():

            # Starting with the child, walk up the parentage, looking
            # at ACLs and bailing out when there is a violation. Look
            # here for illustration:
            # https://github.com/Pylons/substanced/blob/master/substanced/objectmap/__init__.py#L527
            results.append(child) # do nothing for now

        return results
