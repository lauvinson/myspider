"""
js操作与处理工具类

driver = webdriver.Chrome
"""
from selenium.common.exceptions import NoAlertPresentException

from constant.jsconstant import AlertType


def alert(driver, text):
    """
    页面弹窗
    :param driver: 代理窗体
    :param text: 弹窗内容
    """
    driver.execute_script(
        '%s%s%s' % ('alert("', text, '")')
    )
    pass


def alert_accept(driver, t=AlertType.ALERT):
    """
    解决页面弹窗
    :param driver: 代理窗体
    :param t: 弹窗类型
    """
    try:
        if t is AlertType.ALERT:
            driver.switch_to.alert.accept()
        else:
            raise RuntimeError('This type of processing is not defined')
    except NoAlertPresentException:
        pass
