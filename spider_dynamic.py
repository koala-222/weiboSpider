from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from crawler import TirelessCrawler


'''打开网址，预登陆'''
driver = webdriver.Chrome()
print('准备登陆weibo.com')
# 发送请求
wait = WebDriverWait(driver, 10)
driver.get("https://weibo.com/login.php")
# 重要：暂停1分钟进行预登陆，此处填写账号密码及验证
time.sleep(30)


'''输入关键词到搜索框，完成搜索'''
print('开始搜索')
# 使用selector去定位关键词搜索框
s_input = driver.find_element_by_xpath("""//*[@id="app"]/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/span/form/div/input""")
# 向搜索框中传入字段
s_input.send_keys("南海战略态势感知")
s_input.submit()
s_input.send_keys(Keys.ENTER)
# 稍等3秒
time.sleep(3)
# 切换窗口
driver.switch_to.window(driver.window_handles[1])


'''点击进入对应用户主页'''
print("进入用户主页")
icon = driver.find_element_by_xpath("""//*[@id="pl_feedlist_index"]/div[2]/div[1]/div/div[1]/a""")
icon.click()
# 稍等3秒
time.sleep(3)
# 切换窗口
driver.switch_to.window(driver.window_handles[2])


'''爬取全部微博'''
print("开始向下滑动页面，展开微博...")
tireless = TirelessCrawler(driver)
tireless.crawl()


'''写入文件'''
print("将所有微博写入文件")
tireless.save_to("weibo.txt")

