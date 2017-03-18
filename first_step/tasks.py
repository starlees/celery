from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379', broker='amqp://')

@app.task
def add(x, y):
    return x + y
