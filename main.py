import base64

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.jsutils import alert, alert_accept


def main():
    chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:9515')
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver'  # chromedriver的文件位置
    b = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
    b.get('https://www.mihuashi.com/artworks')
    # 设置浏览器的大小
    b.set_window_size(1000, 1000)
    # 显示等待
    waiter = WebDriverWait(b, 3, poll_frequency=0.1, ignored_exceptions=None)
    # 创建 Beautiful Soup 对象
    html = BeautifulSoup(b.page_source, "lxml")
    # 格式化输出 soup 对象的内容
    print(html.prettify)
    builder = ActionChains(b)
    while True:
        try:
            images = b.find_elements_by_class_name('artwork-cell__image')
            for image in images:
                download_image = image
                with open('C:\\Users\\Administrator\\Downloads\\插图\\' + download_image.id + '.png', 'wb') as f:
                    f.write(base64.b64decode(download_image.screenshot_as_base64))
                    f.close()
                builder.key_down(Keys.ESCAPE).perform()
                time.sleep(1)
        except TimeoutException:
            alert(b, "页面元素读取超时")
            time.sleep(3)
            alert_accept(b)
        finally:
            # 休眠一下
            time.sleep(1)


if __name__ == '__main__':
    main()
