[TOC]
# UI自动化
> 基于Pytest+selemiun+Allure接口自动化

## 环境要求：
```
包：
selemiun
allure
pytest 等
```
----
## 模块类的设计
### 构建模块类
> 模块类的说明
- `base.py` 封装元素定位方法，鼠标点击、等待操作等基本方法
- `config.py`读取配置文件
- `login_page.py` 封装登录操作方法
- `mainpage.py` 封装登录之后的主页面的定位方法
- `report.py` 查看测试结果，可展示到页面
- `conftest.py` 封装前置操作方法
- `test_case` 该目录下存放所有测试用例
- `run.py` 定义并执行用例集，生成报告
---
### 配置文件路径
**项目路径**
```python
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的绝对路径的上一级，__file__指当前文件
log_path = os.path.join(prj_path, 'log')  # 数据目录
使用于项目中所需要的文件，读取使用
```
### 关键封装方法代码
> 封装说明
####封装元素定位的操作方法
```python
    # selenium 定位方法，loatetype是根据元素类型进行定位，value是要定位元素的值
    def locate_element(self, loatetype, value)
    # 输入内容方法
    def Input(self, type, value, inputvalue)
    # type是是根据元素类型进行定位，value是要定位元素的值，inputvalue是对输入框需要输入的值
    # 鼠标事件方法，type是是根据元素类型进行定位，value是要定位元素的值，可以对定位后的元素进行点击
    def Click(self, type, value)
    # type是是根据元素类型进行定位，value是要定位元素的值，当定位元素时定位不到，绝对路径中有出现
    # iframe，可以使用该方法进行切换
    def iframe(self,type, value)
     # 切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档
    def default_content(self)
    # 返回页面
     def forward(self)
    # 拖拽滚动条
    def roll(self)
    # 浏览器后退操作
    def back(self):   
    # 隐式等待
    def wait(self,seconds)
    # 这时切换到新窗口
    def Current_handel(self)
    # 获取输入框的值
    def Get_attribute(self, type, value1, value2)    
    # 获取下拉框的文本的值
    def Get_text(self,type, value)
    等多种方法的封装，需要用到方法就要继承该类下的方法

```


#### 封装登录操作方法
```python
def loginsuccess(driver):
    driver.get('http://vip.zj.etmcn.com/Login.aspx')
    elem = driver.find_element_by_id('tbStoreCode')
    ActionChains(driver).double_click(elem).perform()
    driver.find_element_by_id('tbStoreCode').send_keys('003')
    driver.find_element_by_id('tbUserName').send_keys('admin')
    driver.find_element_by_id('tbPassword').send_keys('666666')
    driver.find_element_by_id('Submit1').click()
该方法为了方便用例的执行，单独写出来，为后面的测试用例提供登录方法，可节省编写重复代码的时间
```

#### 封装登录后的页面操作方法
```python
    def clickstudent(self):
    def clickaddstudent(self):
    def clickcoach(self):
    def clickaddstudy(self):
    def clickmoney(self):
    def clicksave(self):
    def stuinfo(self):
    def content(self):
    def iframe_check(self):
    def switch_alert(self):
    def locate(self):
封装登录后页面的操作方法，测试用例中可直接调用
```


#### 封装前置方法
```python
def browser(request):
启用driver，对页面进行操作的必要条件
def pytest_addoption(parser):
增加命令参数，例如headless模式，执行时可以带上参数命令，进行想要的操作
def pytest_runtest_makereport(item, call):
错误截图的方法，出现错误时可截图到报告中查看
def teardown_func(browser):
使用的是同一个driver，执行一个用例后为了方便不关闭浏览器，进行清除cookies操作
```

### 用例
#### 用例1
```
实例化登录后的页面对象（mainpage）
main.clickstudent()  #调用封装mainpage封装的方在登录后的页面点击学员管理按钮
main.clickaddstudent()  #调用封装mainpage封装的方在登录后的页面点击添加学员按钮
main.iframe_check() #因为有iframe，所以要调用切换iframe方法才能定位
main.stuinfo()   #输入需要增加学员的信息
WebDriverWait(browser, 3, 0.5).until(EC.presence_of_element_located((By.ID, 'btnSave')))
#显示等待，等待按钮的出现后再点击，防止出现定位不到的错误
main.clicksave()  #将定位到的按钮，进行点击提交
main.switch_alert()  #出现了alert弹窗，可调用该方法进行处理
name = main.locate().text  #定位增加后的学员名称，可用于验证
assert name == '分分'   #用于验证该学员是否添加成功5
```
#### 用例2
```
loginsuccess(browser)
main = mainpage(browser)  # 实例化登录后的页面对象（mainpage）
main.clickcoach()  # 调用封装mainpage封装的方在登录后的页面点击教学管理按钮
main.clickaddstudy() #点击课程表进入到对应的页面
time.sleep(1)
assert 1 == 1   #举例验证
```


### 执行部分
```
# 执行pytest，生成 Allure 报告需要的数据存在 /report 目录
pytest.main(['-s', '--headless=no','--alluredir', './report/report_json'])
先将数据保存到/report/report_json，该数据是json数据，需要保存
os.system('allure generate ./report/report_json -o ./report/report --clean')
运行的报告出现在/report/report，双击index文件，可打开报告进行查看
执行命令 allure generate ./temp -o ./report_json --clean ，生成测试报告

```
写用例时，可先对页面进行封装部分用例需要的操作，在编写用例中就可以直接调用对页面封装的操作，
即可按照流程一样将该用例写完整，用例写完整后需要有断言，即可选择标志性的元素进行定位，与测试
用例的结果进行对比，对比成功后即可完成一个测试用例。






