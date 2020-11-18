# -*- coding:utf-8 -*-
import random
import time

from commen.base import BaseMethod


class Contract_page(BaseMethod):
    def click_contract(self):
        self.click("link,学员管理")
        self.click('link,我的学员')
        self.switch_frame('name,content')
        self.move_to_element('id,Test')
        self.move_to_element('class,editstate')
        self.sleep_time(0.3)
        self.click("link,签约")

    def sign_contract(self):
        self.switch_frame('xpath,/html/body/div[6]/div[2]/iframe')
        self.move_to_element('class,edit')
        self.get_select_text('id,ddlClassHour', '托班合同')
        self.get_select_text('id,ddlPayType', '现金')
        self.type('id,txtEndDate', '3000-1-1')
        self.scroll_element('id,btnSave')
        self.get_select_text('id,ddlCardType', '王者')
        self.type('id,txtCardNo', self.r_string())
        self.click('id,btnSave')
        self.sleep_time(0.5)
        self.alert_accept()
        self.sleep_time(1.5)

    def last_alert(self):
        self.move_to_element('class,list_th')
        self.click('class,close')

    def auditing_contract(self):
        self.click('link,合同管理')
        self.click('xpath,//*[@id="menuNormal"]/a[3]')
        self.switch_frame('name,content')
        self.move_to_element('id,Test')
        self.clicks('link,[审核]', 0)
        self.scroll_element('id,btnCheck')
        self.click('id,btnCheck')
        self.sleep_time(0.5)
        self.alert_accept()

    def switch_default_content(self):          #切回主文档
        self.switch_default()

    def r_string(self):  # 生成随机字符串
        data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
        # 用时间来做随机播种
        random.seed(time.time())
        # 随机选取数据
        sa = []
        for i in range(20):
            sa.append(random.choice(data))
        salt = "gp_" + ''.join(sa)
        return salt
