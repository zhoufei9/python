
# coding:utf-8
from flask import Blueprint
from lxml import etree
import time
import requests
import json
from setting import SHARES_TOKEN
import tushare as ts
from db.mysqlClient import DB
from application.actions.notice import callme

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
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    return headers


# 更新股票基本信息 每日一次
@investment.route('/collectionShares/')
def collectionShares():
    # 更新所有基础信息
    ts.set_token(SHARES_TOKEN)
    pro = ts.pro_api()
    data = pro.query('stock_basic', exchange='', list_status='L', fields='symbol,name,area,industry,market,list_date')
    items = json.loads(data.to_json(orient='records'))

    shares_list = DB('shares').query('select code from shares').fetchall()
    shares_code_map = []
    for shares in shares_list:
        shares_code_map.append(shares['code'])

    for i in items:
        if i['symbol'] not in shares_code_map:
            DB('shares').insert({'code': i['symbol'], 'name': i['name'], 'area': i['area'], 'industry': i['industry'], 'market': i['market'], 'list_date': i['list_date']})
        # else:
        #     DB('shares').where('code', i['symbol']).update({'area': i['area'], 'industry': i['industry'], 'market': i['market'], 'list_date': i['list_date']})

    print('更新换手率、市盈率、市值等')
    data = ts.get_today_all()

    # print('保存本地')
    # data.to_json('collectionShares.json', orient='records')
    print('to_json')
    items = json.loads(data.to_json(orient='records'))
    print('update shares...')
    for i in items:
        DB('shares').where('code', i['code']).update({'turnoverratio': i['turnoverratio'], 'amount': str(round((int(i['amount'])/100000000), 2)), 'per': i['per'], 'pb': i['pb'], 'mktcap': str(int((int(i['mktcap'])/10000))), 'nmc': str(int((int(i['nmc'])/10000)))})

    return {"code": 0, "msg": 'collectionShares ok'}

# 修复排行榜统计数据
@investment.route('/fixHotTop100/')
def fixHotTop100():
    #todo
    return {"code": 0, "msg": 'fixHotTop100 ok'}

#采集html test
@investment.route('/collectionHotTop100/')
def collectionHotTop100():
    with open('collectionHotTop100.txt') as text:
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

    return {"code": 0, "msg": 'collectionHotTop100 ok'}

@investment.route('/getHotTop100/')
def getHotTop100():
    date = time.strftime("%Y-%m-%d")
    # date = '2021-01-08'

    # retry_count = 5
    # proxy = get_proxy().get("proxy")
    headers = get_headers()
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

    post_headers = headers
    post_headers['Content-Type'] = 'application/json'
    url_params = {"appId":"appId01","globalId":"786e4c21-70dc-435a-93bb-38","pageNo":1,"pageSize":100}
    shares_rk_list = requests.post('https://emappdata.eastmoney.com/stockrank/getAllCurrentList', headers=headers, data=json.dumps(url_params))
    print(shares_rk_list.status_code)

    if shares_rk_list.status_code != 200:
        callme('shares_rk_list requests fail')
        return {"code": 10000, "msg": 'requests fail'}
    data = shares_rk_list.json()


    rk_map = {}
    secids = ''
    for i in data['data']:
        if i['sc'].find('SH') != -1:
            code = i['sc'].replace('SH', '')
            p = '1.'
        else:
            code = i['sc'].replace('SZ', '')
            p = '0.'

        rk_map[code] = i['rk']
        secids += p + code + ','

    secids = secids.rstrip(',')
    get_params = {'ut': 'f057cbcbce2a86e2866ab8877db1d059','fltt': '2','invt': '2','fields': 'f14,f148,f3,f12,f2,f13','secids':secids}
    print(get_params)

    shares_info_list = requests.get('https://push2.eastmoney.com/api/qt/ulist.np/get', headers = get_headers(), params = get_params)
    print(shares_info_list.url)
    print(shares_info_list.status_code)
    if shares_info_list.status_code != 200:
        callme('shares_info_list requests fail')
        return {"code": 10000, "msg": 'requests fail'}

    data = shares_info_list.json()

    check_data = 0
    add_data = []
    for i in data['data']['diff']:
        # 判断第一名是否跟上一个排行数据一致 一致终止执行(可能是误操作重复添加 或者节假日)
        code = i['f12']
        hot_ranking = rk_map[i['f12']]

        if check_data == 0:
            LatestData = DB('sharesHotTop100').where('code', code).order('id desc').find()
            print(LatestData)

            if LatestData:
                if LatestData['code'] == i['f12'] and \
                    LatestData['price'] == str(i['f2']) and \
                    LatestData['up_or_down'] == str(i['f3']) and \
                    LatestData['hot_ranking'] == hot_ranking and \
                    LatestData['date'] == date:
                    return {"code": 0, "msg": '已存在数据 或许今天是休息日'}
            check_data = 1
        add_data.append({'code': i['f12'], 'price': str(i['f2']), 'up_or_down': str(i['f3']), 'hot_ranking': hot_ranking, 'date': date})

    # 批量插入数据  发生错误时忽略 股票代码和日期加了唯一索引 一般是不唯一报错
    success_num = DB('sharesHotTop100').insert(add_data)
    print(success_num)

    if isinstance(success_num, int):
        for i in add_data:
            DB('shares').where('code', i['code']).increment('hotTop100_count')

    return {"code": 0, "msg": 'getHotTop100 ok'}
