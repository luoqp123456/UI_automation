# import time
#
# import allure
#
#
# def _fail_picture(driver):
#     driver.fail_picture()
#
# def fail_picture(self):
#     f = self.get_screenshot_as_file()
#     self.log.debug('失败用例截图:{filename}'.format(filename=f))
#     allure.attach.file(f, '失败用例截图:{filename}'.format(filename=f), allure.attachment_type.PNG)
#
# def get_screenshot_as_file(self):
#     '''在本地截图函数'''
#     try:
#         pic_pth = self.conf.pic_path
#         filename = pic_pth + str(time.time()).split('.')[0] + '.png'
#         filename = filename.replace('\\', '/')
#         self.webdriver.get_screenshot_as_file(filename)
#         self.log.debug('get_screenshot_as_file {filename}'.format(filename=filename))
#         return filename
#     except Exception as e:
#         self.log.error(e)
#         return None