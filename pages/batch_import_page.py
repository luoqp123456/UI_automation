# -*- coding:utf-8 -*-
from commen.base import BaseMethod


class batch_import_page(BaseMethod):
    def click_import(self):

        self.click("link,学员管理")
        self.click("link,批量导入学员")
        self.click("name,content")
        self.switch_frame('name,content')
        self.click("link,未签约学员导入模板")
        self.click("id,linkDown")
        self.move_to_element("id,tbNewData")
        self.type('id,FileUpload1', r'C:\Users\Administrator\Desktop\import.xls')
        self.sleep_time(1)
        self.click("id,btnSaveNew")

