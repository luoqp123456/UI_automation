# -*- coding:utf-8 -*-
from commen.base import BaseMethod


class staffmanage_page(BaseMethod):

    def add_department(self):
        self.waitelement('link_text', 3, '员工管理')
        self.Click("link_text", '员工管理')
        self.waitelement('link_text', 3, '部门信息管理')
        self.Click("link_text", '部门信息管理')

    def add_action(self):
        self.Input('id', 'txtName', '自动化测试')
        self.select_text('id', 'ddlDepartment', '|—校长')
        self.Input('id', 'txtSortID', 0)
        self.Click('id', 'btnAdd')

    def change_iframe(self):
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')

    def accept(self):
        self.alert_accept()