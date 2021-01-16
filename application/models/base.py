# -*- coding: utf-8 -*-
from db.mysqlClient import DB

class ModelsBase(object):
    def __init__(self):
        # 初始化
        print("鸡肋调用")

    def count(self, condition = None, search = None):
        print("count")
        return 1
