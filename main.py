from flask import Flask

app = Flask(__name__)


@app.route('/docker-pull-count')
def get_docker_pull_count():
    return 456789
