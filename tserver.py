import sys
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from server import app  # flask项目

port = sys.argv[1] if len(sys.argv) == 2 else 5000
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
IOLoop.instance().start()
http_server.stop()