# -*- coding: utf-8 -*-
from .base import ModelsBase

class sharesHotTop100(ModelsBase):
    def __init__(self,a):
        self.a = a
        print('111')

    def shuchu(self):
        print('表名sharesHotTop100' + self.a)
        "调用子类构造方法"

