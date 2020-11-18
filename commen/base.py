from time import sleep
import pynput
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from commen.log import Log
from selenium.webdriver.support.select import Select


log = Log()


class BaseMethod(object):

    def __init__(self, driver):
        self.driver = driver

    def split_locator(self, locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',', 1)[0]
        value = locator.split(',', 1)[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
        return locator_dict[by], value

    def wait_element(self, locator, sec=10):
        """
        等待元素出现
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        """
        by, value = self.split_locator(locator)
        try:
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                     message='element not found!!!')
            log.info(u'等待元素：%s' % locator)
            return True
        except TimeoutException:
            return False
        except Exception as e:
            raise e

    def get_element(self, locator, sec=10):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        :return: 元素可找到返回element对象，否则返回False
        """
        if self.wait_element(locator, sec):
            by, value = self.split_locator(locator)
            try:
                element = self.driver.find_element(by=by, value=value)
                log.info(u'获取元素：%s' % locator)
                return element
            except Exception as e:
                raise e
        else:
            return False

    def get_elements(self, locator):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(by=by, value=value))
            log.info(u'获取元素列表：%s' % locator)
            return elements
        except Exception as e:
            raise e

    def get_html(self):
        html = self.driver.execute_script("return document.documentElement.outerHTML")
        log.info(html)
        return html

    def clear(self, locator):
        """
        清除元素中的内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).clear()
        log.info(u'清空内容：%s' % locator)

    def type(self, locator, text):
        """
        在元素中输入内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        ele = self.get_element(locator)
        text = ele.send_keys(text)
        log.info(u'向元素 %s 输入文字：%s' % (locator, text))

    def type_all(self, locator, text):
        """
        在符合条件的所有元素中输入内容，依次循环输入text1,text2……
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        allt = self.get_elements(locator)
        i = 1
        log.info(u'开始执行type_all，共%s个元素' % (len(allt)))
        for ele in allt:
            newtext = text + str(i)
            ele.send_keys(newtext)
            log.info(u'向第 %s 个元素输入文字：%s' % (i, newtext))
            i += 1

    def click(self, locator):
        """
        在元素上单击
        :param repeat: 重复次数标记，不要填写
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        try:
            self.get_element(locator).click()
            log.info(u'点击元素：%s' % locator)
        except Exception as e:
            log.info(u'点击元素：%s 出现错误%s' % (locator, e))

    def clicks(self, locator, index):
        eles = self.get_elements(locator)[index]
        eles.click()

    def sleep_time(self, time):
        sleep(time)

    def click_all(self, locator):
        allc = self.get_elements(locator)
        i = 0
        log.info(u'开始执行click_all，共%s个元素' % (len(allc)))
        for ele in allc:
            self.sleep_time(0.5)
            ele.click()
            i += 1
            log.info(u'点击第 %s 个元素' % i)

    def double_click(self, locator):
        ele = self.get_element(locator)
        ActionChains(self.driver).double_click(ele).perform()
        log.info(u'双击 %s 元素' % locator)

    def move_to_element(self, locator):
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        log.info(u'指向元素%s' % locator)

    def get_attribute(self, locator, attribute):
        value = self.get_element(locator).get_attribute(attribute)
        log.info(u'获取元素 %s 的属性值 %s 为：%s' % (locator, attribute, value))
        return value

    def get_ele_text(self, locator):
        """
        :return: 元素的文本
        """
        ele = self.get_element(locator)
        text = ele.text
        log.info(u'获取元素 %s 的文本为：%s' % (locator, self.get_element(locator).text))
        return text

    def switch_frame(self, locator):
        e = self.get_element(locator)
        self.driver.switch_to.frame(e)
        log.info(u'进入frame：%s' % locator)

    def switch_default(self):
        """
        退出frame返回默认文档
        """
        self.driver.switch_to.default_content()
        log.info(u'退出frame返回默认文档')

    def js(self, script):
        """
        执行JavaScript
        :param script:js语句
        """
        self.driver.execute_script(script)
        log.info(u'执行JS语句：%s' % script)

    def scroll_element(self, locator):
        """
        拖动滚动条至目标元素
        """
        script = "return arguments[0].scrollIntoView();"
        element = self.get_element(locator)
        self.driver.execute_script(script, element)
        log.info(u'滚动至元素：%s' % locator)

    def scroll_top(self):
        """
        滚动至顶部
        """
        self.js("window.scrollTo(document.body.scrollHeight,0)")
        log.info(u'滚动至顶部')

    def scroll_bottom(self):
        """
        滚动至底部
        """
        self.js("window.scrollTo(0,document.body.scrollHeight)")
        log.info(u'滚动至底部')

    def get_element_offset(self, locator):
        """
        获取元素坐标
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: x,y
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        log.info(u'获取元素坐标：%s,%s' % (x, y))
        return x, y

    def get_element_offset_click(self, locator):
        """
        获取元素坐标并点击中间位置，适用于：元素A中套着元素B，元素B无法定位但元素A可以定位
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        loc = element.location
        x = loc['x']
        y = loc['y']
        size = element.size
        width = size['width']
        height = size['height']
        x += width
        y += height
        self.click_offset(x, y)

    def click_offset(self, x, y):
        """
        点击坐标
        :param x: x坐标'
        :param y: y坐标'

        """
        ActionChains(self.driver).move_by_offset(x, y).click().perform()
        log.info(u'点击坐标%s,%s' % (x, y))

    def forward(self):      #页面向前
        self.driver.forward()

    def back(self):         #页面后退
        self.driver.back()

    def refresh(self):     #刷新页面
        self.driver.refresh()

    def close(self):       #关闭当前页
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

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

        # 获取下拉框的文本的值

    def get_select_text(self, locator, text):
        ele = self.get_element(locator)
        Select(ele).select_by_visible_text(text)
        text = ele.text
        return text

    def get_select_value(self, locator, value):      #通过value属性
        m = self.get_element(locator)
        Select(m).select_by_value(value)

        # 校验按钮是否为选中状态
    def Is_selected(self, locator):
        self.get_element(locator).is_selected()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        text = str(alert.text)
        log.info(u'alert提示为：%s' % text)
        alert.accept()
        return text

    def alert_text(self):
        a = self.driver.switch_to.alert
        b = a.text()
        log.info(b)

    def alert_dimiss(self):
        alert = self.driver.switch_to.alert
        alert.dimiss()

    def wait_alert(self, waittime):
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, waittime).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = str(alert.text)
        log.info(u'alert提示为：%s' % text)
        alert.accept()

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




