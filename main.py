import docker


def start_server():
    docker.app.run(debug=True)


if __name__ == '__main__':
    start_server()
