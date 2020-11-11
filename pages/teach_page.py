# -*- coding:utf-8 -*-
from time import sleep

from commen.base import BaseMethod
from commen.log import Log

log = Log()

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
        self.select_text('id','ddlLessonSeries', '舞蹈系列')
        self.select_text('id','ddlLesson', '拉丁舞课程')
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

    def select_student(self):
        self.Click('class_name', 'bDiv')
        page = self.locate_element('class_name', 'pageCount')
        page_sum = page.text
        sum_page = int(page_sum)
        j = 1
        for j in range(sum_page):
            ele_list = self.find_elements('tag_name', 'tr')
            for i in range(1, len(ele_list)):
                if i < 30:
                    ele = self.locate_element('xpath', f'//*[@id="Test"]/tbody/tr[{i}]')
                    ele1 = f'//*[@id="Test"]/tbody/tr[{i}]'
                    self.scroll_element('xpath', ele1)
                    loca = self.locate_element('xpath', f'//*[@id="Test"]/tbody/tr[{i}]/td[3]/div/a[1]')
                    name = loca.text
                    if name == '自动化测试排课':
                        raw = f'//*[@id="Test"]/tbody/tr[{i}]'
                        xpath = raw + '/td[1]/div/a'
                        self.Click('xpath', xpath)
                        break
                    else:
                        log.info(ele.text)
                        log.info('页面没有找到数据')
                else:
                    self.movefloat('class_name', 'pGroup')
                    self.Click('class_name', 'pButton')
            j += 1
            sleep(0.5)

    def close1(self):
        self.Click('class_name', 'close')

    def click_save(self):
        self.Click('id', 'cbMsg')
        self.Click('id', 'cbWx')
        self.Click('id', 'cbWxTeacher')
        self.Click('id', 'btnAppSave')

    def accept_alert(self):
        self.alert_accept()

    def loca_course(self):
        self.Click('css', '[title="班级:拉丁舞课程"]')
        self.Click('id', 'btnDel')

    def daily_management(self):
        self.waitelement('link_text', 3, '教学管理')
        self.Click("link_text", '教学管理')
        self.waitelement('link_text', 3, '日常教务管理')
        self.Click('link_text','日常教务管理')
        self.waitelement('link_text', 3, '学员上课请假')
        self.Click('link_text', '学员上课请假')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.movefloat('id', 'Test')
        self.Click('xpath','/html/body/div[6]/div[2]/iframe')
        self.default_content()
        self.iframe('class_name', 'content')
        self.Input('id', 'txtReason', '123123')