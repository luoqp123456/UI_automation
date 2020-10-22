# # -*- coding:utf-8 -*-
# import pytest
# from pages.action_page import Action_page
# from pages.login_page import loginsuccess
#
#
# class Test_actioncenter:
#     def test_addaction(self, browser, log_up):
#         try:
#             log_up.info('测试用例：活动中心添加活动')
#             loginsuccess(browser)
#             ac = Action_page(browser)
#             ac.addaction()
#         except Exception as e:
#             print("Exception happening :" + str(e))
#             raise
#
#
# if __name__ == '__main__':
#     pytest.main(['-v', 'test_actioncenter.py'])