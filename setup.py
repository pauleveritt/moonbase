from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'deform>=2.0a2',
    'pyramid_tm',
    'pyramid_sqlalchemy',
    'waitress'
]
setup(name='moonbase',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = moonbase:main
      [console_scripts]
      initialize_moonbase_db = moonbase.scripts.initializedb:main
      """
      )
