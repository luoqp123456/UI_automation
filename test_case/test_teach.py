# -*- coding:utf-8 -*-
from time import sleep
import allure
import pytest
from pages.login_page import loginsuccess
from pages.teach_page import Teach_page


class Test_teachstu:
    @allure.description('添加课程，后取消排课')
    def test_add_course(self, browser, log_up):        #登录后点击添加学员按钮
        try:
            log_up.info('测试用例：添加课程')
            loginsuccess(browser)
            teacher = Teach_page(browser)  # 实例化登录后的页面对象（mainpage）
            teacher.addcourse()
            teacher.switch_default_content()
            teacher.switch_frame()
            teacher.select_student()
            teacher.switch_default_content()
            teacher.close1()
            teacher.frame()
            teacher.click_save()
            sleep(0.5)
            teacher.accept_alert()
            teacher.loca_course()
            teacher.accept_alert()
            sleep(0.5)
            teacher.accept_alert()
        except Exception as e:
            print("Exception happening :" + str(e))
            raise

    # def test_teach_manage(self, browser, log_up):        #登录后点击添加学员按钮
    #     try:
    #         log_up.info('测试用例：添加课程')
    #         loginsuccess(browser)
    #         teacher = Teach_page(browser)  # 实例化登录后的页面对象（mainpage）
    #         teacher.daily_management()
    #
    #     except Exception as e:
    #         print("Exception happening :" + str(e))
    #         raise


if __name__ == '__main__':
    pytest.main(['-v','test_teach.py'])








