from time import sleep
import pynput
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from commen.log import Log
from selenium.webdriver.support.select import Select


log = Log()


class BaseMethod(object):

    def __init__(self, driver):
        self.driver = driver

    # selenium 定位方法
    def locate_element(self, loatetype, value):
        if loatetype == 'id':
            el = self.driver.find_element_by_id(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'name':
            el = self.driver.find_element_by_name(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'class_name':
            el = self.driver.find_element_by_class_name(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'tag_name':
            el = self.driver.find_elements_by_tag_name(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'link':
            el = self.driver.find_element_by_link_text(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'css':
            el = self.driver.find_element_by_css_selector(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'partial_link':
            el = self.driver.find_element_by_partial_link_text(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        elif loatetype == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            log.info(u'元素类型 %s ,属性值 %s' % (loatetype, value))
            return el
        else:
            print(None)

    def locate_elements(self, loatetype, value, index):
        if (loatetype == 'id'):
            el = self.driver.find_elements_by_id(value)[index]
        elif (loatetype == 'name'):
            el = self.driver.find_elements_by_name(value)[index]
        elif (loatetype == 'class_name'):
            el = self.driver.find_elements_by_class_name(value)[index]
        elif (loatetype == 'tag_name'):
            el = self.driver.find_elements_by_tag_name(value)[index]
        elif (loatetype == 'link'):
            el = self.driver.find_elements_by_link_text(value)[index]
        elif (loatetype == 'css'):
            el = self.driver.find_elements_by_css_selector(value)[index]
        elif (loatetype == 'partial_link'):
            el = self.driver.find_elements_by_partial_link_text(value)[index]
        elif (loatetype == 'xpath'):
            el = self.driver.find_elements_by_xpath(value)[index]
        return el if el else None

    def Input(self, type, value, inputvalue):     # 输入内容方法
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)
            log.info(u'输入内容，元素类型 %s ,属性值 %s ， 输入值%s' % (type, value, inputvalue))


        # 鼠标事件方法一
    def Click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "id":
            self.driver.find_element_by_id(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "name":
            self.driver.find_element_by_name(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))
        else:
            self.driver.find_element_by_css_selector(value).click()
            log.info(u'鼠标点击，元素类型 %s ,属性值 %s ' % (type, value))



    def click_css(self, value):
        self.driver.find_element_by_css_selector(value).click()

    def click_css2(self, value, index):
        self.driver.find_element_by_css_selector(value)[index].click()


        # 鼠标事件方法二
    def Clicks(self,type, value, index):
        if type == "xpath":
            self.driver.find_elements_by_xpath(value)[index].click()
        elif type == "class_name":
            self.driver.find_elements_by_class_name(value)[index].click()
        elif type == "id":
            self.driver.find_elements_by_id(value)[index].click()
        elif type == "name":
            self.driver.find_elements_by_name(value)[index].click()
        elif type == "link_text":
            self.driver.find_elements_by_link_text(value)[index].click()
        elif type == "partial_link_text":
            self.driver.find_elements_by_partial_link_text(value)[index].click()

    def iframe(self,type, value):
        if type == "xpath":
            frame = self.driver.find_element_by_xpath(value)
            self.driver.switch_to.frame(frame)
            log.info(u'切换iframe，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "name":
            frame =self.driver.find_element_by_name(value)
            self.driver.switch_to.frame(frame)
            log.info(u'切换iframe，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "tag_name":
            frame =self.driver.find_element_by_tag_name(value)
            self.driver.switch_to.frame(frame)
            log.info(u'切换iframe，元素类型 %s ,属性值 %s ' % (type, value))

    def iframe_parent(self, value):    #切回父iframe
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name(value))

    def default_content(self):
        self.driver.switch_to.default_content()       #切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档
        log.info('切换回主文档')

    def forward(self):      #页面向前
        self.driver.forward()

    def back(self):         #页面后退
        self.driver.back()

    def refresh(self):     #刷新页面
        self.driver.refresh()

    def close(self):       #关闭当前页
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_element(self, type, value):     #true是到顶部，false到底部
             # 拖动滚动条至目标元素
        if type == 'xpath':
            element = self.driver.find_elements_by_xpath(value)
            self.driver.execute_script("return arguments[0].scrollIntoView(false);", element)
        elif type == 'id':
            element = self.driver.find_element_by_id(value)
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def scroll_down(self):       #滚动到最底部
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def scroll_up(self):       #滚动到最顶部
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight,0)')

    def roll(self):          #滚动条针对整个HTML
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)

    def roll_body(self):       #滚动条针对整个body
        js = "var q=document.body.scrollTop=10000"
        self.driver.execute_script(js)

        # 隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    #     # 保存图片
    # def get_windows_img(self):
    #     """
    #     在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
    #     """
    #     file_path = os.path.dirname(os.path.abspath('../common')) + '/screenshots/'
    #     rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    #     screen_name = file_path + rq + '.png'
    #     try:
    #         self.driver.get_screenshot_as_file(screen_name)
    #     except NameError as e:
    #         self.get_windows_img()

    def Current_handel(self):
        # 这时切换到新窗口
        now_handle = self.driver.current_window_handle  # 获取当前窗口句柄
        # print(now_handle)  # 输出当前获取的窗口句柄
        return now_handle

    def handel(self):
        all_handles = self.driver.window_handles
        log.info(self.Current_handel())
        for i in all_handles:
            if i == self.Current_handel():
                log.info('同一个')
                print('同一个WIN')
            else:
                self.driver.switch_to.window(all_handles[1])
                log.info('多个')
                print('多个')
        # 切换到新的handle上
        # self.driver.switch_to.window(all_handles[1])

        # 验证元素是否存在
    def Check_element(self,type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value)
            log.info(u'验证元素，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "id":
            self.driver.find_element_by_id(value)
            log.info(u'验证元素，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "name":
            self.driver.find_element_by_name(value)
            log.info(u'验证元素，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "link_text":
            self.driver.find_element_by_link_text(value)
            log.info(u'验证元素，元素类型 %s ,属性值 %s ' % (type, value))
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)
            log.info(u'验证元素，元素类型 %s ,属性值 %s ' % (type, value))


        # 获取输入框的值
    def Get_attribute(self, type, value1, value2):
        if type == "xpath":
            value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            log.info(u'获取输入框值，元素类型 %s ,属性值 %s ,获取内容 %s' % (type, value1, value2))
            return value
        elif type == "name":
            value = self.driver.find_element_by_name(value1).get_attribute(value2)
            log.info(u'获取输入框值，元素类型 %s ,属性值 %s ,获取内容 %s' % (type, value1, value2))
            return value
        elif type == "link_text":
            value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            log.info(u'获取输入框值，元素类型 %s ,属性值 %s ,获取内容 %s' % (type, value1, value2))
            return value
        elif type == "class_name":
            value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            log.info(u'获取输入框值，元素类型 %s ,属性值 %s ,获取内容 %s' % (type, value1, value2))
            return value
        elif type == "id":
            value = self.driver.find_element_by_id(value1).get_attribute(value2)
            log.info(u'获取输入框值，元素类型 %s ,属性值 %s ,获取内容 %s' % (type, value1, value2))
            return value

        # 获取下拉框的文本的值

    def Get_text(self,type, value):
        if type == "xpath":
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text

    def select_text(self, type, value1,value2):         #通过选项可见文本
        if type == 'id':
            m = self.driver.find_element_by_id(value1)
            Select(m).select_by_visible_text(value2)
        elif type == 'css':
            m = self.driver.find_element_by_id(value1)
            Select(m).select_by_visible_text(value2)

    def select_value(self, value1, value2):      #通过value属性
        m = self.driver.find_element_by_id(value1)
        Select(m).select_by_value(value2)


    # def check_text(self,Xpath, value):
    #         WebElementtext = self.driver.findElement(By.id)
    #         self.text.getText().contains("文字")
    #         return
    #         self.login("183******44", "a1234567****")
    #         time.sleep(3)
    #         # 断言方法1：
    #         slef.text = self.driver.find_element_by_xpath(Xpath).text
    #
    #         Text = str(value)
    #
    #          "//*[@id='settingForHover']/div/div[1]/span[2]"
    #         StringpageTitle = str(self.driver.title())
    #         self.assertEqual(Text, value)

        # # 鼠标移动点击机制
    def Move_action(self, type, value):
        if type == "xpath":
            xm = self.driver.find_element_by_xpath(value)
            webdriver.ActionChains(webdriver.Chrome()).click(xm).perform()
        elif type == "id":
            xm = self.driver.find_element_by_id(value)
            webdriver.ActionChains(webdriver.Chrome()).click(xm).perform()
        elif type == "name":
            xm = self.driver.find_element_by_name(value)
            webdriver.ActionChains(webdriver.Chrome()).click(xm).perform()
        elif type == "link_text":
            xm = self.driver.find_element_by_link_text(value)
            webdriver.ActionChains(webdriver.Chrome()).click(xm).perform()

        # 校验按钮是否为选中状态
    def Is_selected(self, type, value):
        if type == "id":
            self.driver.find_element_by_id(value).is_selected()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).is_selected()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).is_selected()
        elif type == "name":
            self.driver.find_element_by_name(value).is_selected()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()

    def movefloat(self, type, value ):
        # 定位到要悬停的元素
        if type == "id":
            move = self.driver.find_element_by_id(value)
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
        elif type == "xpath":
            move = self.driver.find_element_by_xpath(value)
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
        elif type == "class_name":
            move = self.driver.find_element_by_class_name(value)
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
        elif type == "name":
            move = self.driver.find_element_by_name(value)
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
        elif type == "link_text":
            move = self.driver.find_element_by_link_text(value)
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()

    def movefloat_class(self, type, value, index):
        if type == 'class_name':
            move = self.driver.find_elements_by_class_name(value)[index]
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()
        elif type == 'css':
            move = self.driver.find_elements_by_css_selector(value)[index]
            # 对定位到的元素执行悬停操作
            ActionChains(self.driver).move_to_element(move).perform()

    def alert_accept(self):
        self.driver.switch_to.alert.accept()     #新

    def alert_text(self):
        a = self.driver.switch_to.alert
        b = a.text()
        log.info(b)

    def alert_dimiss(self):
        alert = self.driver.switch_to.alert  # 新
        alert.dimiss()

    def wait_alert(self, waittime):
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, waittime).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def waitelement(self, type, waittime, value):
        if type == "id":
            WebDriverWait(self.driver,waittime).until(lambda x: x.find_element_by_id(value))
        elif type == "name":
            WebDriverWait(self.driver, waittime).until(lambda x: x.find_element_by_name(value))
        elif type == "class_name":
            WebDriverWait(self.driver, waittime).until(lambda x: x.find_element_by_class_name(value))
        elif type == "xpath":
            WebDriverWait(self.driver, waittime).until(lambda x: x.find_element_by_xpath(value))
        elif type == "link_text":
            WebDriverWait(self.driver, waittime).until(lambda x: x.find_element_by_link_text(value))
        else:
            print('元素类型错误')

    def clear(self, by, locator):               # """清理数据"""
        element = self.locate_element(by, locator)
        element.clear()

    def get_url(self):
        print(self.driver.current_url)
        log.info(u'获取输入框值，元素类型 %s ' % (self.driver.current_url))

    def keybord(self, value):
        control = pynput.keyboard.Controller()
        sleep(1)
        control.type(value)
        sleep(1)
        control.press(pynput.keyboard.Key.enter)
        control.release(pynput.keyboard.Key.enter)
        sleep(5)




    # def split_locator(self, locator):
    #  #分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
    #  #:param locator: 定位方法+定位表达式组合字符串，如'css,.username'
    #  #:return: locator_dict[by], value:返回定位方式和定位表达式
    #     by = locator.split(',')[0]
    #     value = locator.split(',')[1]
    #     locator_dict = {
    #     'id': 'id',
    #     'name': 'name',
    #     'class': 'class name',
    #     'tag': 'tag name',
    #     'link': 'link text',
    #     'plink': 'partial link text',
    #     'xpath': 'xpath',
    #     'css': 'css selector',
    #     }
    #     if by not in locator_dict.keys():
    #         raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
    #     return locator_dict[by], value

    # def get_element(self, locator, sec=60):
    #          # 获取一个元素
    #          # :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
    #          # :param sec:等待秒数
    #          # :return: 元素可找到返回element对象，否则返回False
    #     if self.wait_element(locator, sec):
    #         by, value = self.split_locator(locator)
    #         print(by, value)
    #         try:
    #             element = self.driver.find_element(by=by, value=value)
    #             log.info(u'获取元素：%s' % locator)
    #             return element
    #         except Exception as e:
    #             raise e
    #     else:
    #         return False
