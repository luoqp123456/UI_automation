from time import sleep

from commen.base import BaseMethod


class mainpage(BaseMethod):

    def addstudent(self):
        self.waitelement('link_text', 3, '学员管理')
        self.Click("link_text", '学员管理')
        self.waitelement('link_text', 3, '添加学员')
        self.Click("link_text", '添加学员')
        self.waitelement('name', 3, 'content')
        self.iframe('name', 'content')
        self.waitelement('id', 3, 'txtRealName')
        self.Input('id', 'txtRealName', '分分1')
        self.Input('id', 'txtMobile', '15548757837')
        self.keybord_click()

    def clicksave(self):
        self.waitelement('id', 3, 'btnSave')
        self.Click('id', 'btnSave')

    def switch_alert(self):
        self.alert_accept()

    def locate(self):
        name = self.locate_element('id', 'lbRealName')
        return name

    def clickcoach(self):
        self.Click("link_text", '教学管理')

    def clickaddstudy(self):
        self.Click("link_text", '课程表')

    def clickmoney(self):
        self.Click("link_text", '活动中心')

    def keybord_click(self):
        self.Click('id', 'divShowupload')
        self.keybord('C:\\Users\\Administrator\\Desktop\\timg.jpg')


