# -*- coding:utf-8 -*-
import allure
import pytest
from pages.login_page import loginsuccess
from pages.staffmanage_page import staffmanage_page


class Test_add_department:
    def test_click_add(self, browser, log_up):
        try:
            log_up.info('测试用例：添加部门')
            loginsuccess(browser)
            staff = staffmanage_page(browser)
            staff.add_department()
            staff.change_iframe()
            staff.add_action()
            staff.alert_accept()
        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_staff_department.py'])