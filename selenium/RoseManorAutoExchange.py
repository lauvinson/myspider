import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
权帅的玫瑰庄园
"""
while True:
    try:
        # 重复使用浏览器
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # 创建Chrome浏览器对象，chromedriver需要放在chrome同级目录
        browser = webdriver.Chrome('S:/Program Files (x86)/Google/Chrome/Application/chromedriver',
                                   chrome_options=chrome_options)
        # 设置浏览器的大小
        browser.set_window_size(1000, 800)
        # 带上已授权cookie
        cookie = [
            {'name': '__cookie_sz_yi_userid_143', 'value': 'dTkyMjUwMWQyZmRjMTNhZmM2NTkwN2I0M2M5ZmJhZDBm'},
            {'name': 'openid', 'value': 'u922501d2fdc13afc65907b43c9fbad0f'},
            {'name': 'PHPSESSID', 'value': 'fa2e151d7e108646f2388780d529ab18'}
        ]
        for c in cookie:
            new = dict(c, **{
                "domain": ".514544.com",
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False,
            })
            browser.add_cookie(new)
        # 发起浏览器请求
        browser.get("http://www.514544.com/dist/index.html#/center")

        # 刷新浏览器
        browser.refresh()

        # 获取元素需要注意页面加载是否完成,
        # 点击MGY下面的查看按钮
        time.sleep(1)
        mgyView = browser.find_elements_by_class_name('src-components-center-center---btncha---2JAzQ_1')[0]
        mgyView.click()
        # 点击财务管理>>玫瑰庄园钱包明细>>兑换
        time.sleep(1)
        exchangeEntry = browser.find_element_by_xpath('html/body/div/div/section/div/span')
        exchangeEntry.click()
        # 展开兑换玫瑰种类
        time.sleep(1)
        rose_list = browser.find_element_by_xpath('html/body/div/div[1]/section[2]/div[2]')
        rose_list.click()
        # 选择第一种玫瑰种类
        time.sleep(1)
        rose = browser.find_element_by_xpath('html/body/div/div[1]/div[1]/div[1]/a[1]')
        rose.click()
        # 提交兑换
        # excute = browser.find_element_by_xpath('html/body/div/div[1]/section[2]/div[3]')
        # excute.click()
    finally:
        # 休眠一下
        time.sleep(3)
