"""
Creates local_files.db and creates files table.
"""
from app import db
db.create_all()
