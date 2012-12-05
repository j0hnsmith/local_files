import json
from flask import make_response
from flask.ext.classy import FlaskView
from app import app
from app.models import File
from utils import DateTimeJsonEncoder


class FilesApi(FlaskView):
    route_base = '/api/v1/files'

    def index(self):
        """
        Provide a collection of all files, maps to /api/v1/files/
        """
        files = [f.as_dict() for f in File.query.all()]
        if not files:
            response = make_response(json.dumps({'error': 'no files found'}), 404)
        else:
            response = make_response(json.dumps(files, cls=DateTimeJsonEncoder))

        response.headers['Content-Type'] = 'application/json'
        return response

    def get(self, id):
        """
        Provides resource details for a file with a given id, maps to /api/v1/files/<id>
        """
        f = File.query.get(id)
        if not f:
            response = make_response(json.dumps({'error': 'no file found with id %s' % id}), 404)
        else:
            response = make_response(json.dumps(f.as_dict(), cls=DateTimeJsonEncoder))

        response.headers['Content-Type'] = 'application/json'
        return response

FilesApi.register(app)
