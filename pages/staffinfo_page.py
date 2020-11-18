# -*- coding:utf-8 -*-
from time import sleep
from commen.base import BaseMethod
from commen.log import Log

log = Log()


class staffinfo_page(BaseMethod):

    def department(self):
        self.click('link,员工管理')

    def add_department(self):
        self.click('link,员工信息管理')

    def add_staff(self):
        self.click('link,员工信息添加')

    def delete_locate(self):
        sum_page = int(self.page())
        j = 1
        for j in range(sum_page):
            ele_list = self.get_elements('css,[abbr="UserName"]')
            for i in range(1, len(ele_list)):
                ele = self.get_element(f'xpath,//*[@id="Test"]/tbody/tr[{i}]/td[2]')
                ele1 = f'//*[@id="Test"]/tbody/tr[{i}]/td[2]'
                self.scroll_element(f'xpath, {ele1}')
                if ele.text == 'zidonghuaceshi':
                    raw = f'//*[@id="Test"]/tbody/tr[{i}]'
                    xpath = raw + '/td[1]/div/a[3]'
                    self.click(f'xpath,{xpath}')
                    self.accept()
                    break
                else:
                    log.info(ele.text)
                    log.info('页面没有找到数据')
            j += 1
            self.click('class,pNext')
            sleep(0.5)

    def add_data(self):
        sum_page = int(self.page())
        j = 1
        for j in range(sum_page):
            ele_list = self.get_elements('css,[abbr="UserName"]')
            for i in range(1, len(ele_list)):
                if i < 30:
                    ele = self.get_element(f'xpath, //*[@id="Test"]/tbody/tr[{i}]/td[2]')
                    ele1 = f'//*[@id="Test"]/tbody/tr[{i}]/td[2]'
                    self.scroll_element(f'xpath, {ele1}')
                    if ele.text == 'zidonghuaceshi':
                        return ele.text
                    else:
                        log.info(ele.text)
                        log.info('页面没有找到数据')
                else:
                    self.click('class,pNext')
            j += 1
            sleep(0.5)

    def page(self):
        pagenum = self.get_element('xpath,//*[@id="form1"]/div[3]/div[6]/div[1]/div[5]/span/span[2]')
        page_sum = pagenum.text
        return page_sum

    def change_table(self):
        self.move_to_element('id,Test')

    def change_iframe(self):
        self.switch_frame('name,content')

    def accept(self):
        self.wait_alert(5)

    def add(self):
        self.change_iframe()
        self.type('id,txtName', 'zidonghuaceshi')
        self.type('id,txtRealName', '自动化测试')
        self.type('id,txtMobile', '15521283809')
        self.get_select_text('id,ddlPosition', '|—|—校长')
        self.clicks('name,cbRight', 0)
        self.click('id,btnSave')
        self.sleep_time(1)

    def get_alert_text(self):
        text = str(self.alert_text())
        return text

    def content(self):
        self.switch_default()

    def alert_acc(self):
        self.alert_accept()