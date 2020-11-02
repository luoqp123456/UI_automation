# -*- coding:utf-8 -*-
import re
from time import sleep
from commen.base import BaseMethod
from commen.log import Log

log = Log()


class staffinfo_page(BaseMethod):

    def department(self):
        self.waitelement('link_text', 3, '员工管理')
        self.Click("link_text", '员工管理')

    def add_department(self):
        self.waitelement('link_text', 5, '员工信息管理')
        self.Click("link_text", '员工信息管理')

    def add_staff(self):
        self.waitelement('link_text', 3, '员工信息添加')
        self.Click("link_text", '员工信息添加')

    def delete_locate(self):
        sum_page = int(self.page())
        j = 1
        for j in range(sum_page):
            ele_list = self.find_elements('css', '[abbr="UserName"]')
            for i in range(1, len(ele_list)):
                ele = self.locate_element('xpath', f'//*[@id="Test"]/tbody/tr[{i}]/td[2]')
                ele1 = f'//*[@id="Test"]/tbody/tr[{i}]/td[2]'
                self.scroll_element('xpath', ele1)
                if ele.text == 'zidonghuaceshi':
                    raw = f'//*[@id="Test"]/tbody/tr[{i}]'
                    xpath = raw + '/td[1]/div/a[3]'
                    self.Click('xpath', xpath)
                    self.accept()
                    break
                else:
                    log.info(ele.text)
                    log.info('页面没有找到数据')
            j += 1
            self.Click('class_name', 'pNext')
            sleep(0.5)

    def add_data(self):
        sum_page = int(self.page())
        j = 1
        for j in range(sum_page):
            ele_list = self.find_elements('css', '[abbr="UserName"]')
            for i in range(1, len(ele_list)):
                ele = self.locate_element('xpath', f'//*[@id="Test"]/tbody/tr[{i}]/td[2]')
                ele1 = f'//*[@id="Test"]/tbody/tr[{i}]/td[2]'
                self.scroll_element('xpath', ele1)
                if ele.text == 'zidonghuaceshi':
                    return ele.text
                else:
                    log.info(ele.text)
                    log.info('页面没有找到数据')
            j += 1
            self.Click('class_name', 'pNext')
            sleep(0.5)

    def page(self):
        pagenum = self.locate_element('xpath', '//*[@id="form1"]/div[3]/div[6]/div[1]/div[5]/span/span[2]')
        page_sum = pagenum.text
        return page_sum

    def change_table(self):
        self.waitelement('id', 3, 'Test')
        self.movefloat('id', 'Test')

    def change_iframe(self):
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')

    def accept(self):
        self.wait_alert(5)

    def add(self):
        self.change_iframe()
        self.Input('id', 'txtName', 'zidonghuaceshi')
        self.Input('id', 'txtRealName', '自动化测试')
        self.Input('id', 'txtMobile', '15521283809')
        self.select_text('id', 'ddlPosition', '|—|—校长')
        self.Clicks('name', 'cbRight', 0)
        self.Click('id', 'btnSave')
        self.accept()
        sleep(0.5)

    def get_alert_text(self):
        text = str(self.alert_text())
        return text

    def content(self):
        self.default_content()