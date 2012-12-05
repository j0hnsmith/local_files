import json
import os
import unittest
from config import PROJECT_ROOT
from app import app, db, tasks
from app.models import File


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        resp = self.app.get('/')
        self.assertIn('Hello World', resp.data)

    def test_run_tasks_page(self):
        resp = self.app.get('/run-task-to-get-files')
        self.assertIn('task added', resp.data)

    def test_get_local_files(self):
        # check no files to start with
        count = File.query.count()
        self.assertEqual(count, 0)

        # now scan for files and check we get some
        tasks.get_local_files()
        count = File.query.count()
        self.assertTrue(count > 0)

    def test_api_all_files(self):
        # check error response works
        resp = self.app.get('/api/v1/files/')
        data = json.loads(resp.data)
        self.assertTrue(data.has_key('error'))

        # now scan for files and ensure response contains some
        tasks.get_local_files()
        resp = self.app.get('/api/v1/files/')
        data = json.loads(resp.data)
        self.assertTrue(len(data) > 0)

    def test_api_single_file(self):
        tasks.get_local_files()
        # check error response works
        resp = self.app.get('/api/v1/files/9876543210')
        data = json.loads(resp.data)
        self.assertTrue(data.has_key('error'))

        # now check for good response
        resp = self.app.get('/api/v1/files/1')
        data = json.loads(resp.data)
        self.assertIn('name', data)
        self.assertIn('dir_path', data)

if __name__ == '__main__':
    unittest.main()
