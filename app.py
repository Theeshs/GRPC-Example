from flask import Flask
from server import serve

# listner = Listener()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    serve()
    # app.run()
