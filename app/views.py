from app import app, tasks

@app.route('/')
def home():
    return 'Hello World!<br/><a href="/run-task-to-get-files">run task in background to get files</a>'

@app.route('/run-task-to-get-files')
def run_task_to_get_files():
    tasks.get_local_files.apply_async()
    return 'task added<br/><a href="/api/v1/files">view all files via api</a>'



