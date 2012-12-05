import os
from datetime import datetime
from celery import Celery
from celery.task.base import task
from config import PROJECT_ROOT, BROKER_URL
from app import db
from app.models import File


celery = Celery('tasks', broker=BROKER_URL)

@task
def get_local_files():
    """
    Recursively gets all files from directory PROJECT_ROOT and lower and adds to/updates the db.
    """
    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
        for filename in filenames:
            mode, ino, dev, nlink, uid, gid, size, accessed, modified, created = os.stat(os.path.join(dirpath, filename))
            f = File.query.filter_by(name=filename, dir_path=dirpath).first()

            if f:
                # file already exists, update it with latest values
                f.size = size
                f.uid = uid
                f.gid = gid
                f.accessed = datetime.utcfromtimestamp(accessed)
                f.modified = datetime.utcfromtimestamp(modified)
                f.created = datetime.utcfromtimestamp(created) # could have been deleted and recreated
                f.last_seen = datetime.now()

            else:
                # file not in db, add it
                f = File(
                    name=filename,
                    dir_path=dirpath,
                    size=size,
                    uid=uid,
                    gid=gid,
                    accessed=datetime.utcfromtimestamp(accessed),
                    modified=datetime.utcfromtimestamp(modified),
                    created=datetime.utcfromtimestamp(created),
                    last_seen=datetime.now()
                )
            db.session.add(f)
            db.session.commit() # safer to commit each time but possibly unneccessary



