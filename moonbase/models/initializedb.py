import os
import sys
import transaction

from pyramid.config import Configurator
from pyramid_sqlalchemy import Session
from pyramid_sqlalchemy.meta import metadata
from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from .folder import RootFolder, Folder
from .document import Document


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    # Usage and configuration
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')

    # Make the database with schema and default data
    with transaction.manager:
        metadata.create_all()
        root = RootFolder(name='',
                      title='Moonbase Demo',
                      __acl__=[
                          ['Allow', ['paul'], 'view']
                      ]
                      )
        Session.add(root)
        f1 = root['f1'] = Folder(
            title='Folder 1',
            __acl__=[
                ['Allow', ['shane'], 'view']
            ]
        )
        f1['da'] = Document(title='Document 1A')
