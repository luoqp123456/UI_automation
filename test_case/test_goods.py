# -*- coding:utf-8 -*-
import pytest
from pages.goods_page import Goods_page
from pages.login_page import loginsuccess


class Test_goods:
    def test_addgoods(self, browser, log_up):
        try:
            log_up.info('测试用例：物品添加')
            loginsuccess(browser)
            gp = Goods_page(browser)
            gp.addgoods()
        except Exception as e:
            print("Exception happening :" + str(e))
            raise


if __name__ == '__main__':
    pytest.main(['-v', 'test_goods.py'])