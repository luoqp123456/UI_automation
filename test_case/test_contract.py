# -*- coding:utf-8 -*-
from time import sleep
import allure
import pytest
from pages.contract_page import Contract_page
from pages.login_page import loginsuccess


class Test_contract:
    @allure.description('签约合同')
    def test_contract(self, browser, log_up):        #登录后点击添加学员按钮
        try:
            log_up.info('测试用例：签约合同')
            loginsuccess(browser)
            cont = Contract_page(browser)  # 实例化登录后的页面对象（mainpage）
            cont.click_contract()
            cont.switch_default_content()
            cont.sign_contract()
            cont.switch_default_content()
            sleep(1)
            cont.last_alert()
            sleep(0.5)
            cont.auditing_contract()
        except Exception as e:
            print("Exception happening :" + str(e))
            raise

    # def test_contract22222(self, browser, log_up):        #登录后点击添加学员按钮
    #     try:
    #         log_up.info('测试用例：签约合同')
    #         loginsuccess(browser)
    #         cont = Contract_page(browser)  # 实例化登录后的页面对象（mainpage）
    #         cont.click_contract()
    #         cont.switch_default_content()
    #         cont.sign_contract()
    #         sleep(1)
    #         cont.switch_default_content()
    #         sleep(1)
    #         cont.last_alert()
    #         sleep(0.5)
    #         cont.auditing_contract()
    #
    #     except Exception as e:
    #         print("Exception happening :" + str(e))
    #         raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_contract.py'])