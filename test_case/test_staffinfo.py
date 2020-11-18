# -*- coding:utf-8 -*-
import allure
import pytest
from pages.login_page import loginsuccess
from pages.staffinfo_page import staffinfo_page


class Test_staff_info:

    def test_click_delete01(self, browser, log_up):
        try:
            log_up.info('测试用例：添加员工')
            loginsuccess(browser)
            staff = staffinfo_page(browser)
            staff.department()
            staff.add_staff()
            staff.add()
            staff.accept()
            staff.content()
            staff.department()
            staff.add_department()
            staff.change_iframe()
            staff.change_table()
            staff.add_data()
        except Exception as e:
            print(u'Exception is happening:' % e)

    def test_click_delete02(self, browser, log_up):
        try:
            log_up.info('测试用例：请假登记')
            loginsuccess(browser)
            staff = staffinfo_page(browser)
            staff.department()
            staff.add_department()
            staff.change_iframe()
            staff.change_table()
            staff.delete_locate()
            staff.alert_acc()

        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_staffinfo.py'])