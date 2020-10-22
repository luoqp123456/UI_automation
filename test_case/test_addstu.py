from time import sleep
import allure
import pytest
from pages.MainPage import mainpage
from pages.login_page import loginsuccess


class Test_Addstudents():

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
            # with allure.step('截图验证'):
            #     browser.save_screenshot("./Picture/学员名称.png")
            #     allure.attach.file("./Picture/学员名称.png", "截图", attachment_type=allure.attachment_type.PNG)
            assert name == '分分'
        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_addstu.py'])










