# -*- coding:utf-8 -*-
from time import sleep
from commen.base import BaseMethod


class Contract_page(BaseMethod):
    def click_contract(self):
        self.waitelement('link_text', 3, '学员管理')
        self.Click("link_text", '学员管理')
        self.waitelement('link_text', 3, '我的学员')
        self.Click("link_text", '我的学员')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('id', 3, 'Test')
        self.movefloat('id','Test')
        self.waitelement('class_name', 3, 'editstate')
        self.movefloat('class_name','editstate')
        sleep(0.3)
        self.Click("link_text", '签约')


    def sign_contract(self):
        self.iframe('xpath', '/html/body/div[6]/div[2]/iframe')
        self.waitelement('class_name', 3, 'edit')
        self.movefloat('class_name', 'edit')
        self.select_text('id', 'ddlClassHour', '托班合同')
        self.select_text('id', 'ddlPayType', '现金')
        self.Input('id', 'txtEndDate', '3000-1-1')
        self.scroll_element('id', 'btnSave')
        self.Click('id', 'btnSave')
        sleep(1)
        self.accept_alert()

    def last_alert(self):
        self.waitelement('class_name', 5, 'floatBox')
        self.movefloat('class_name', 'floatBox')
        self.waitelement('class_name', 5, 'list_th')
        self.movefloat('class_name', 'list_th')
        self.Click('class_name', 'close')

    def auditing_contract(self):
        self.waitelement('link_text', 3, '合同管理')
        self.Click("link_text", '合同管理')
        self.Click("xpath", '//*[@id="menuNormal"]/a[3]')
        self.waitelement('name', 5, 'content')
        self.iframe('name', 'content')
        self.waitelement('id', 3, 'Test')
        self.movefloat('id', 'Test')
        self.Clicks('link_text', '[审核]', 0)
        self.scroll_element('id', 'btnCheck')
        self.Click('id', 'btnCheck')
        sleep(0.5)
        self.accept_alert()

    def frame(self):
        self.iframe('tag_name', 'iframe')

    def switch_default_content(self):          #切回主文档
        self.default_content()

    def accept_alert(self):
        self.alert_accept()

    # def ram(self):
    #     str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    #     import random
    #     while True:
    #         code = ''
    #         for i in range(4):
    #             num = random.randint(0, len(str1) - 1)
    #             code += str1[num]
    #         return code