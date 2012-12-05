import os
from app import db


class File(db.Model):
    """
    Model to represent a file.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    dir_path = db.Column(db.String(1023))
    size = db.Column(db.Integer) # in bytes
    uid = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    accessed = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    created = db.Column(db.DateTime)
    last_seen = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('dir_path', 'name'),
    )

    def __repr__(self):
        return "<File %r, %r, %r, %r, %r, %r, %r, %r, %r>" % (
            self.name,
            self.dir_path,
            self.size,
            self.uid,
            self.gid,
            self.accessed,
            self.modified,
            self.created,
            self.last_seen
        )

    @property
    def full_path(self):
        return os.path.join(self.dir_path, self.name)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
