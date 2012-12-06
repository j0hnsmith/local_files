from flask import render_template
from app import app, tasks

@app.route('/')
def home():
    return render_template('base.html', h1='Hello World!', content='<a href="/run-task-to-get-files">run task in background to get files</a>')

@app.route('/run-task-to-get-files')
def run_task_to_get_files():
    tasks.get_local_files.apply_async()
    return render_template('base.html', h1='Task Added', content='<a href="/api/v1/files">view all files via api</a>')



