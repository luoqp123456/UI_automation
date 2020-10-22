import os
import pytest


if __name__ == '__main__':

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    # pytest.ini.main(['-xcopy','.\allure-report\history .\allure-results\history /e /Y /I'])
    pytest.main(['-v', '-n=auto', '--headless=no', '--alluredir', './report/allure-xml'])  #生成数据
    os.system('allure generate ./report/allure-xml -o ./report/allure-result --clean') #生成测试报告
    # os.system('xcopy .\\allure-result\\history .\\allure-report\\history /e /Y /I')  #趋势图
    # os.system('copy environment.xml report\\allure-xml\\environment.xml')     #环境
    # os.system('copy categories.json report\\allure-xml\\categories.json')     #类型
    # os.system('allure open ./report/allure-result')



