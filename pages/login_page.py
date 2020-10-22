from selenium.webdriver.common.action_chains import ActionChains

def loginsuccess(driver):

    driver.get('http://vip.zj.etmcn.com/Login.aspx')
    elem = driver.find_element_by_id('tbStoreCode')
    ActionChains(driver).double_click(elem).perform()
    driver.find_element_by_id('tbStoreCode').send_keys('003')
    driver.find_element_by_id('tbUserName').send_keys('admin')
    driver.find_element_by_id('tbPassword').send_keys('666666')
    driver.find_element_by_id('Submit1').click()
