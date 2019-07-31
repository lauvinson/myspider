import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.jsutils import alert, alert_accept
from utils.strutils import parse_name_equals_value_to_dict, parse_name_equals_value_to_dict_map, \
    parse_linux_conf_to_dict

"""
权帅的玫瑰庄园
"""

# 驱动配置
driver_conf_file = open(file='../../../driver.conf')
driver_arr = driver_conf_file.read().split("; ")
driver_conf_dict = parse_linux_conf_to_dict('../../../driver.conf')

# 重复使用浏览器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", driver_conf_dict['debugger_address'])

# 创建Chrome浏览器对象，chromedriver需要放在chrome同级目录

browser = webdriver.Chrome(driver_conf_dict['chrome_webdriver_path'], chrome_options=chrome_options)
# 设置浏览器的大小
browser.set_window_size(1000, 1000)
# 显示等待
waiter = WebDriverWait(browser, 3, poll_frequency=0.1, ignored_exceptions=None)
cookie = open(file='../cookie.txt')
cookies = cookie.read().split("; ")
print('##################################\nCookie:')
for co in cookies:
    element = parse_name_equals_value_to_dict(co)
    print(element)
    new = dict(element, **{
        "domain": ".514544.com",
        "expires": "",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False,
    })
    browser.add_cookie(new)
# 发起浏览器请求
# browser.get("http://www.514544.com/dist/index.html#/center")
# # 获取元素需要注意页面加载是否完成,
# # 点击MGY下面的查看按钮
# time.sleep(0.5)
# mgyView = browser.find_elements_by_class_name('src-components-center-center---btncha---2JAzQ_1')[0]
# print(mgyView.text)
# mgyView.click()
# # 点击财务管理>>玫瑰庄园钱包明细>>兑换
# time.sleep(0.5)
# exchangeEntry = browser.find_element_by_xpath('html/body/div/div/section/div/span')
# print(exchangeEntry.text)
# exchangeEntry.click()
browser.get("http://www.514544.com/dist/index.html#/exchange")
# 执行计数器
cycle_c = 0
while True:
    try:
        browser.refresh()
        # 展开兑换玫瑰种类
        rose_list = waiter.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div/div[1]/section[2]/div[2]')))
        print(rose_list.text)
        rose_list.click()
        # 选择第一种玫瑰种类
        try:
            rose = waiter.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div/div[1]/div[1]/div[1]/a[1]')))
            print(rose.text)
            rose.click()
            # 提交兑换
            # excute = waiter.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div/div[1]/section[2]/div[3]')))
            # excute.click()
        except NoSuchElementException:
            print('无可选玫瑰，跳过选择')
        cycle_c = cycle_c + 1
    except TimeoutException:
        alert(browser, "页面元素读取超时")
        time.sleep(3)
        alert_accept(browser)
    finally:
        # 休眠一下
        print("执行次数:", cycle_c)
