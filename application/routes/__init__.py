# -*- coding: utf-8 -*-
from application.actions.proxy import proxy
from application.actions.investment import investment
from application.actions.github import github
from application.actions.video import video


def init_app(app):
    app.register_blueprint(proxy, url_prefix='/proxy')
    app.register_blueprint(investment, url_prefix='/investment')
    app.register_blueprint(github, url_prefix='/github')
    app.register_blueprint(video, url_prefix='/video')


