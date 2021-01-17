# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from application.actions.notice import callme

customException = Blueprint('customException',__name__)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        print(message)
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message

@customException.app_errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@customException.app_errorhandler(500)
def error(error):
    callme('500 error url:' + request.url)
    return {"code": 0, "msg": 'fixHotTop100 ok'}