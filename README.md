install
-------
* create virtualenv and enter
* install requirements `pip install -r requirements.txt`
* create db `python init_db.py`
* run tests `python tests.py` (not fully comprehensive)

start celery
----------
* `celery -A app.tasks worker --loglevel=info --concurrency=1`

start app
-------
* `python run_app.py`

visit site
----------
* go to http://localhost:5000/ in your browser
* follow link to run background task to inspect filesystem
* follow link to view api

api
---
* all files http://localhost:5000/api/v1/files/
* single file http://localhost:5000/api/v1/files/<id> where <id> is integer primary key of file

