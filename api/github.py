# -*- coding: utf-8 -*-
# !/usr/bin/env python
from flask import Blueprint
import requests
import pygal
from pygal.style import LightColorizedStyle as lcs,LightenStyle as ls

github = Blueprint('github',__name__)

@github.route('/getTop30StarPythonProject/')
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
