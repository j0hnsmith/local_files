import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(PROJECT_ROOT, 'local_files.db')
DEBUG=True
