from time import sleep
import allure
import pytest
from pages.MainPage import mainpage
from pages.login_page import loginsuccess


class Test_Addstudents():
    @allure.description('添加学员')
    def test_add_success(self, browser, log_up):        #登录后点击添加学员按钮
        try:
            log_up.info('测试用例：添加学员')
            loginsuccess(browser)
            main = mainpage(browser)  # 实例化登录后的页面对象（mainpage）
            main.addstudent()
            main.clicksave()
            sleep(0.5)
            main.switch_alert()
            name = main.locate().text
            assert name == '分分'
        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_addstu.py'])










