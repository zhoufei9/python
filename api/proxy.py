# -*- coding: utf-8 -*-
# !/usr/bin/env python

from flask import Blueprint, jsonify, request
import requests
from werkzeug.wrappers import Response
from handler.proxyHandler import ProxyHandler
from helper.proxy import Proxy

proxy = Blueprint('proxy',__name__)


proxy_handler = ProxyHandler()

class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)

proxy.response_class = JsonResponse


@proxy.route('/')
def index():
    api_list = {
    'get': u'get an useful proxy',
    'pop': u'get and delete an useful proxy',
    # 'refresh': u'refresh proxy pool',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
    'get_status': u'proxy number'
}
    return api_list


@proxy.route('/get/')
def get():
    proxy = proxy_handler.get()
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@proxy.route('/pop/')
def pop():
    proxy = proxy_handler.pop()
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@proxy.route('/refresh/')
def refresh():
    # TODO refresh会有守护程序定时执行，由api直接调用性能较差，暂不使用
    return 'success'


@proxy.route('/get_all/')
def getAll():
    proxies = proxy_handler.getAll()
    return jsonify([_.to_dict for _ in proxies])


@proxy.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    status = proxy_handler.delete(Proxy(proxy))
    return {"code": 0, "src": status}


@proxy.route('/get_status/')
def getStatus():
    status = proxy_handler.getCount()
    return status
