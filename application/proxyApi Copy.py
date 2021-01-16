# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     ProxyApi.py
   Description :   WebApi
   Author :       JHao
   date：          2016/12/4
-------------------------------------------------
   Change Activity:
                   2016/12/04: WebApi
                   2019/08/14: 集成Gunicorn启动方式
                   2020/06/23: 新增pop接口
-------------------------------------------------
"""
__author__ = 'JHao'

import platform
from werkzeug.wrappers import Response
from flask import Flask, jsonify#, request

from util.six import iteritems
from handler.proxyHandler import ProxyHandler
from handler.configHandler import ConfigHandler
from helper.proxy import Proxy

app = Flask(__name__)
conf = ConfigHandler()
proxy_handler = ProxyHandler()

from application.actions.investment import investment
from application.proxy import proxy

app.register_blueprint(investment, url_prefix='/investment')
app.register_blueprint(proxy, url_prefix='/proxy')

class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse

api_list = {
    'get': u'get an useful proxy',
    'pop': u'get and delete an useful proxy',
    # 'refresh': u'refresh proxy pool',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
    'get_status': u'proxy number'
}


@app.route('/')
def index():
    return api_list


@app.route('/get/')
def get():
    proxy = proxy_handler.get()
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@app.route('/pop/')
def pop():
    proxy = proxy_handler.pop()
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@app.route('/refresh/')
def refresh():
    # TODO refresh会有守护程序定时执行，由api直接调用性能较差，暂不使用
    return 'success'


@app.route('/get_all/')
def getAll():
    proxies = proxy_handler.getAll()
    return jsonify([_.to_dict for _ in proxies])


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    status = proxy_handler.delete(Proxy(proxy))
    return {"code": 0, "src": status}


@app.route('/get_status/')
def getStatus():
    status = proxy_handler.getCount()
    return status

from urllib import request
from lxml import etree
import json
import re
import ssl


# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


import requests
import pygal
from pygal.style import LightColorizedStyle as lcs,LightenStyle as ls


def get_headers():
    """
    返回请求头信息
    :return:
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/74.0.3729.169 Safari/537.36"
    }
    print(headers)
    return headers


def get_url_content(url,ip):
    """
    获取指定url的请求内容
    :param url:
    :return:
    """
    content = ''
    headers = get_headers()
    res = request.Request(url, headers=headers)
    try:
        resp = request.urlopen(res, timeout=10)
        content = resp.read().decode('utf-8')
    except Exception as e:
        print('exception: %s' % e)
    return content


def parse_content(content):
    """
    解析网页
    :param content:
    :return:
    """
    movie = {}
    html = etree.HTML(content)
    try:
        info = html.xpath("//div[@id='info']")[0]
        movie['director'] = info.xpath("./span[1]/span[2]/a/text()")[0]
        movie['screenwriter'] = info.xpath("./span[2]/span[2]/a/text()")[0]
        movie['actors'] = '/'.join(info.xpath("./span[3]/span[2]/a/text()"))
        movie['type'] = '/'.join(info.xpath("./span[@property='v:genre']/"
                                            "text()"))
        movie['initialReleaseDate'] = '/'.\
            join(info.xpath(".//span[@property='v:initialReleaseDate']/text()"))
        movie['runtime'] = \
            info.xpath(".//span[@property='v:runtime']/text()")[0]

        def str_strip(s):
            return s.strip()

        def re_parse(key, regex):
            ret = re.search(regex, content)
            movie[key] = str_strip(ret[1]) if ret else ''

        re_parse('region', r'<span class="pl">制片国家/地区:</span>(.*?)<br/>')
        re_parse('language', r'<span class="pl">语言:</span>(.*?)<br/>')
        re_parse('imdb', r'<span class="pl">IMDb链接:</span> <a href="(.*?)" '
                         r'target="_blank" rel="nofollow">')
    except Exception as e:
        print('解析异常: %s' % e)
    return movie


def spider(ip):
    """
    爬取豆瓣前100部热门电影
    :return:
    """
    recommend_moives = []
    movie_api = 'https://movie.douban.com/j/search_subjects?' \
                'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend' \
                '&page_limit=30&page_start=0'
    content = get_url_content(movie_api,ip)
    json_dict = json.loads(content)
    subjects = json_dict['subjects']
    for subject in subjects:
        content = get_url_content(subject['url'],ip)
        movie = parse_content(content)
        movie['title'] = subject['title']
        movie['rate'] = subject['rate']
        recommend_moives.append(movie)
        print(len(recommend_moives))
    print(recommend_moives)


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

@app.route('/getTop30StarPythonProject/')
def getTop30StarPythonProject():
    #执行API调用并存储响应,language:python为选择python语言
    url='https://api.github.com/search/repositories?q=language:python&sort=stars'
    r=requests.get(url)

    #打印200表示请求成功
    print(r.status_code)

    #将API响应存储在一个变量中
    response_dict=r.json()

    #创建两个列表来存放x轴与y轴数据
    names,stars=[],[]
    for i in response_dict['items']:
            print(i['name'])
            print(i['stargazers_count'])
            names.append(i['name'])
            stars.append(i['stargazers_count'])

    #可视化
    my_style=ls('#0eb1ff',base_style=lcs)
    chart=pygal.Bar(style=my_style,x_label_rotation=145,show_legend=False)
    chart.title='GitHub 30个star最多的python项目'
    chart.x_labels=names
    chart.add('',stars)
    chart.render_to_file('Top30StarPythonProject.svg')
    return {"code": 0, "msg": 'GitHub 30个star最多的python项目 Top30StarPythonProject.svg已生成'}

@app.route('/getHtml/')
def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    print(proxy)
    spider(proxy)
    # 删除代理池中代理
    # delete_proxy(proxy)
    return {"code": 10000, "msg": 'xxx'}

def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


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
