# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/4/13 7:18
from selenium.webdriver.common.by import By


class IndexLocator:
    # 注销
    logOut = ("注销按钮", (By.XPATH, '//span[text()="注销"]'))
    # 普通送达菜单
    ptsd = ("送达任务菜单按钮", (By.XPATH, '//li[contains(text(),"送达任务")]'))
