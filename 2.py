from appium import webdriver
import time

desired_caps = {
                'platformName': 'Android',
                'deviceName': '192.168.228.101:5555',
                'platformVersion': '7.0',
                'appPackage': 'com.example.android.contactmanager', 
                'appActivity': 'ContactManager',
                'unicodeKeyboard': True, 
                'resetKeyboard': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_xpath("//*[@resource-id='com.example.android.contactmanager:id/showInvisible']").click()
time.sleep(10)
'''
driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").clear()
driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").send_keys('appium测试')

driver.find_element_by_id("float_search_or_cancel").click()
driver.find_element_by_id("floating_action_button").click()
'''
driver.quit()

