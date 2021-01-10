
# coding:utf-8
from flask import Blueprint, request
from lxml import etree
import time
import requests
from db.mysqlClient import DB

investment = Blueprint('investment',__name__)
 
def get_proxy():
    return requests.get("http://127.0.0.1:5010/proxy/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/proxy/delete/?proxy={}".format(proxy))

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
    
    return headers

@investment.route('/collectionHotTop100/')
def collectionHotTop100():
    #date = time.strftime("%Y-%m-%d") 
    date = '2021-01-08'

    # retry_count = 5
    # proxy = get_proxy().get("proxy")
    # headers = get_headers()
    # print(proxy)
    # print(headers)
    # 
    # while retry_count > 0:
    #     try:
    #         html = requests.get('https://vipmoney.eastmoney.com/collect/stockranking/pages/ranking/list.html?fc=SZ002571', proxies={"https": "https://{}".format(proxy)}, headers=headers)
    #         # 使用代理访问
    #         print(html)
    #         retry_count = 0
    #     except Exception:
    #         retry_count -= 1
    #         print(retry_count)
    #         if retry_count == 0:
    #             # 删除代理池中代理
    #             delete_proxy(proxy)
    #             return {"code": 10000, "msg": proxy + '请求失败已删除'}
    
    with open('Text-1.txt') as text:
        textz = text.read()
    html = etree.HTML(textz)
    items = html.xpath('//div[@class="item"]')
 
    shares_list = DB('shares').query('select code from shares').fetchall()
    shares_code_map = []
    for shares in shares_list:
        shares_code_map.append(shares['code'])  

    check_data = 0
    add_data = []
    for item in items:
        # result = etree.tostring(item)
        # print(result.decode("utf-8"))

        hot_ranking = item.xpath('./ul/li[1]/span/text()')[0] if item.xpath('./ul/li[1]/span/text()') else ''
        name = item.xpath('./ul/li[2]/span/text()')[0] if item.xpath('./ul/li[2]/span/text()') else ''
        code = item.xpath('./ul/li[2]/p/span/text()')[0] if item.xpath('./ul/li[2]/p/span/text()') else ''
        price = item.xpath('./ul/li[3]/text()')[0] if item.xpath('./ul/li[3]/text()') else ''
        up_or_down = item.xpath('./ul/li[4]/text()')[0] if item.xpath('./ul/li[4]/text()') else ''
        hot = item.xpath('./div/p/text()')[0] if item.xpath('./div/p/text()') else ''
        
        # 判断第一名是否跟上一个排行数据一致 一致终止执行
        if check_data == 0:
            LatestData = DB('sharesHotTop100').where('code', code).order('id desc').find()
            print(LatestData)
            if LatestData :
                if LatestData['code'] == code and \
                LatestData['price'] == price and \
                LatestData['up_or_down'] == up_or_down and \
                LatestData['hot_ranking'] == hot_ranking and \
                LatestData['hot'] == hot and LatestData['date'] == date :
                    return {"code": 0, "msg": '已存在数据 或许今天是休息日'}
            check_data = 1
            
        add_data.append({'code': code,'price': price,'up_or_down': up_or_down,'hot_ranking': hot_ranking,'hot': hot,'date': date})
       
        # 不存在的股票新增
        if code not in shares_code_map:
           DB('shares').insert({'code': code, 'name': name})
    
    # 批量插入数据  发生错误时忽略 股票代码和日期加了唯一索引 一般是不唯一报错
    success_num = DB('sharesHotTop100').insert(add_data)
    print(success_num)
    
    if isinstance(success_num, int):
        for i in add_data:
            DB('shares').where('code', i['code']).increment('hotTop100_count')
   
    return {"code": 0, "msg": 'xxx'}