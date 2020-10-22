# -*- coding:utf-8 -*-
import allure
import pytest
from pages.batch_import_page import batch_import_page
from pages.login_page import loginsuccess


class Test_import:
    def test_import(self, browser, log_up):
        try:
            log_up.info('测试用例：签约合同')
            loginsuccess(browser)
            bi = batch_import_page(browser)
            bi.click_import()
        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_import.py'])