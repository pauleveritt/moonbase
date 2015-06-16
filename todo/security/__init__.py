from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

USERS = {'editor': 'editor',
         'viewer': 'viewer'}
GROUPS = {'editor': ['group:editors']}


def groupfinder(userid, request):
    # We could get users from the database using a
    # SQLAlchemy query
    if userid in USERS:
        return GROUPS.get(userid, [])


def includeme(config):
    authn_policy = AuthTktAuthenticationPolicy(
        config.registry.settings['tutorial.secret'],
        callback=groupfinder,
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.scan('.views')