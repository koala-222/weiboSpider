from selenium.webdriver.common.keys import Keys
import time
import json


class TirelessCrawler(object):
    def __init__(self, driver):
        # selenium驱动器
        self.driver = driver
        # 保留所有微博文本
        self.array = set()

    def crawl_current_content(self):
        number = 1
        while True:
            # 当前微博
            try:
                cur = self.driver.find_element_by_xpath("""//*[@id="scroller"]/div[1]/div[{}]""".format(number))
            except:
                break
            # 对应文字区域
            try:
                content = cur.find_element_by_class_name("""detail_wbtext_4CRf9""")
            except Exception as e:
                print("[WARNING] 找不到微博内容！")
                raise ValueError
            try:
                span = content.find_element_by_class_name("""expand""")
                span.click()
                time.sleep(1)
            except:
                pass
            finally:
                print(content.text[:30] + " ...... " + content.text[-30:])
                self.array.add(content.text)
            number += 1

    def crawl(self):
        """展开微博并保存，滑动页面，直到底端"""
        for i in range(40):
            self.crawl_current_content()
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(5)

    def save_to(self, file):
        """以JSON格式写入文件"""
        with open(file, "w", encoding="utf-8") as f:
            text = json.dumps(list(self.array), ensure_ascii=False)
            f.write(text)

