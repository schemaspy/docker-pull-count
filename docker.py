from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/pull-count')
def get_docker_pull_count():
    r = requests.get("https://hub.docker.com/v2/repositories/schemaspy/schemaspy/")

    pull_count = 0

    if r.ok:
        response = r.json()
        pull_count = response['pull_count']

    return str(pull_count)
