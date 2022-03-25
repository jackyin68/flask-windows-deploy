from flask import Flask, send_from_directory
from flask import request
import os
import sys

path = os.path.dirname(sys.path[0])
if path and path not in sys.path:
    sys.path.append(path)

app = Flask(__name__)


@app.route('/')
def index():
    return "Congratuation, access Flask API successfully!!!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True,use_reloader=False)
