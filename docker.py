from flask import Flask
import requests
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/pull-count', methods=['GET', ' OPTIONS'])
@cross_origin()
def get_docker_pull_count():
    r = requests.get("https://hub.docker.com/v2/repositories/schemaspy/schemaspy/")

    pull_count = 0

    if r.ok:
        response = r.json()
        pull_count = response['pull_count']

    return str(pull_count)
