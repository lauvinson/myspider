##这里是selenium的使用

###启动代理窗体
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

###使用代理窗体

    # 重复使用浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # 创建Chrome浏览器对象，chromedriver需要放在chrome同级目录
    browser = webdriver.Chrome('S:/Program Files (x86)/Google/Chrome/Application/chromedriver',
                               chrome_options=chrome_options)
