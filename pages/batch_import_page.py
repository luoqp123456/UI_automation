# -*- coding:utf-8 -*-
from time import sleep

from commen.base import BaseMethod


class batch_import_page(BaseMethod):
    def click_import(self):
        self.waitelement('link_text', 3, '学员管理')
        self.Click("link_text", '学员管理')
        self.waitelement('link_text', 3, '批量导入学员')
        self.Click("link_text", '批量导入学员')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('link_text', 5, '未签约学员导入模板')
        self.Click("link_text", '未签约学员导入模板')
        self.waitelement('id', 3, 'linkDown')
        self.Click("id", 'linkDown')
        self.movefloat('id', 'tbNewData')
        self.waitelement('id', 3, 'FileUpload1')
        self.Input('id', 'FileUpload1', r'C:\Users\Administrator\Desktop\import.xls')
        sleep(1)
        self.Click('id', 'btnSaveNew')

