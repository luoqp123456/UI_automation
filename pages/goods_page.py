# -*- coding:utf-8 -*-
from time import sleep
from commen.base import BaseMethod


class Goods_page(BaseMethod):
    def addgoods(self):
        self.waitelement('link_text', 3, '资产管理')
        self.Click("link_text", '资产管理')
        self.Click("link_text", '物品添加')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('id', 3, 'tbProductName')
        self.Input('id', 'tbProductName', '自动化测试')
        self.waitelement('id', 3, 'tbPurchasePrice')
        self.Input('id', 'tbPurchasePrice', '5')
        self.Input('id', 'tbSalePrice', '10')
        self.scroll_element('id', 'btnsave')
        self.Click("id", 'btnsave')
        self.wait_alert(3)



