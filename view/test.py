"""
可视化操作
手动启动 chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
"""
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# 重复使用浏览器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome('C:/Users/vinson/AppData/Local/Google/Chrome SxS/Application/chromedriver',
                           chrome_options=chrome_options)

# 2.通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

# 3.刷新浏览器
browser.refresh()

# 4.设置浏览器的大小
browser.set_window_size(1400, 800)

# 5.设置链接内容
element = browser.find_element_by_link_text("新闻")
element.click()

element = browser.find_element_by_link_text("习近平以三“新”续写中朝友谊新篇章")
element.click()

# 获取当前的windo handle
current_window = browser.current_window_handle
# 获得当前所有打开的windo handle
all_handles = browser.window_handles
for handle in all_handles:
    if handle != current_window:
        browser.switch_to.window(handle)

# 获取当前打开的网页html内容
html = browser.page_source

# 创建 Beautiful Soup 对象
soup = BeautifulSoup(html)

# 格式化输出 soup 对象的内容
print(soup.prettify)

# 清除
browser.quit()
