from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/docker-pull-count')
def get_docker_pull_count():
    return 456789
