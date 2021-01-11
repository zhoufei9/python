# -*- coding: utf-8 -*-
# !/usr/bin/env python

import platform
from flask import Flask, jsonify
from util.six import iteritems
from werkzeug.wrappers import Response

from handler.configHandler import ConfigHandler

from api.investment import investment
from api.proxy import proxy
from api.github import github
from api.video import video


app = Flask(__name__)
conf = ConfigHandler()

app.register_blueprint(investment, url_prefix='/investment')
app.register_blueprint(proxy, url_prefix='/proxy')
app.register_blueprint(github, url_prefix='/github')
app.register_blueprint(video, url_prefix='/video')


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)

app.response_class = JsonResponse

def runFlask():
    if platform.system() == "Windows":
        app.run(host=conf.serverHost, port=conf.serverPort)
    else:
        import gunicorn.app.base

        class StandaloneApplication(gunicorn.app.base.BaseApplication):

            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super(StandaloneApplication, self).__init__()

            def load_config(self):
                _config = dict([(key, value) for key, value in iteritems(self.options)
                                if key in self.cfg.settings and value is not None])
                for key, value in iteritems(_config):
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        _options = {
            'bind': '%s:%s' % (conf.serverHost, conf.serverPort),
            'workers': 4,
            'accesslog': '-',  # log to stdout
            'access_log_format': '%(h)s %(l)s %(t)s "%(r)s" %(s)s "%(a)s"'
        }
        StandaloneApplication(app, _options).run()


if __name__ == '__main__':
    runFlask()
