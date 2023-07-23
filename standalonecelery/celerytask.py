from celery import Celery

app = Celery('app2')
app.config_from_object('celeryconfig')


@app.task
def add_numbers():
    return
