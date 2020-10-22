# -*- coding:utf-8 -*-
from commen.base import BaseMethod


class Teach_page(BaseMethod):
    def addcourse(self):
        self.waitelement('link_text', 3, '教学管理')
        self.Click("link_text", '教学管理')
        self.Click("link_text", '课程表')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('class_name', 3, 'contentTd')
        self.movefloat_class('class_name','contentTd', 6)
        self.waitelement('class_name', 3, 'addCourseMemberCount')
        self.Clicks("class_name", 'addCourseMemberCount', 6)
        self.select_text('id','ddlLessonSeries', '语言系列')
        self.select_text('id','ddlLesson', '韩语课程')
        value = 'cc8fe4a9-2eea-4908-a07b-04d6833f5070'
        self.select_value('ddlClassroom', value)
        self.Clicks('class_name', 'list_td', 0)

    def frame(self):
        self.iframe('name', 'content')

    def switch_default_content(self):          #切回主文档
        self.default_content()

    def switch_frame(self):       #切到iframe
        self.iframe('xpath', '/html/body/div[6]/div[2]/iframe')

    def switch_table_clickstu(self):
        self.Click('class_name', 'bDiv')
        self.Clicks('link_text', '[选择]', 0)

    def close1(self):
        self.Click('class_name', 'close')

    def click_save(self):
        self.Click('id', 'cbMsg')
        self.Click('id', 'cbWx')
        self.Click('id', 'cbWxTeacher')
        self.Click('id', 'btnAppSave')

    def accept_alert(self):
        self.alert_accept()

    def dimiss(self):
        self.alert_dimiss()

    def loca_course(self):
        self.Click('css', '[title="班级:韩语课程"]')
        self.Click('id', 'btnDel')
