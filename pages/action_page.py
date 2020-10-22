# -*- coding:utf-8 -*-
from time import sleep

from commen.base import BaseMethod


class Action_page(BaseMethod):
    def addaction(self):
        self.waitelement('link_text', 3, '活动中心')
        self.Click("link_text", '活动中心')
        self.Click("link_text", '活动添加')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('id', 3, 'txtDoTitle')
        self.Input('id', 'txtDoTitle', '自动化活动')
        self.waitelement('id', 3, 'txtDoTitle')
        self.select_text('id', 'ddlDoType', '比赛')
        self.Input('id', 'txtMemberCount', '10')
        self.Input('id', 'txtStartDate', '2030-01-01')
        self.Input('id', 'txtEndDate', '2030-01-02')
        sleep(0.5)
        self.scroll_element('id', 'cbMsg')
        self.Click('id', 'cbMsg')
        self.Click('id', 'cbWx')
        self.Click('id', 'btnSave')
        self.alert_accept()
        sleep(0.5)
        self.waitelement('link_text', 3, '[删除]')
        self.Click("link_text", '[删除]')
        self.alert_accept()
        sleep(0.5)
        self.alert_accept()

    def frame(self):
        self.iframe('name', 'content')

    def switch_default_content(self):          #切回主文档
        self.default_content()
