import os
import sys

from flask import Flask, send_from_directory,render_template

path = os.path.dirname(sys.path[0])
if path and path not in sys.path:
    sys.path.append(path)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")
static_folder = "web/static"
template_folder = "web"
app = Flask(__name__,static_url_path='',static_folder=static_folder,template_folder=template_folder)


@app.route('/')
def index():
    # return send_from_directory(root, "index.html")
    return render_template('index.html')
    # return "Congratuation, access Flask API successfully!!!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True,use_reloader=False)
