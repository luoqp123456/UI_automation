# import os
# import sys
# from selenium.webdriver.chrome.options import Options
# import allure
# import pytest
# from selenium import webdriver
# from commen.log import Log
#
# driver = None
# log = None
#
#
# def pytest_addoption(parser):
#     """定义命令行参数"""
#     parser.addoption("--headless", action="store", default="no", help="set headless option yes or no")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def browser(request):
#     global driver
#     headless = request.config.getoption('--headless')
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     # chrome_options.add_argument('--disable-gpu')
#     if headless == 'yes' or sys.platform.startswith('lin'):
#         if driver is None:
#             # 创建浏览器对象
#             driver = webdriver.Chrome(options=chrome_options)
#             yield driver
#             driver.quit()
#     else:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         yield driver
#         driver.quit()
#
#
# @pytest.fixture(scope="session", autouse=True)
# def log_up():
#     global log
#     if log is None:
#         log = Log()
#     return log
#
#
# @pytest.fixture(scope="function", autouse=True)
# def teardown_func(browser):
#     yield
#     browser.delete_all_cookies()
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         with allure.step('添加失败截图...'):
#             allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
#
