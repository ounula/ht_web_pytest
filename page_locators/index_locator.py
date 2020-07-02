# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium.webdriver.common.by import By


class IndexLocator:
    # 注销
    logOut = ("注销按钮", (By.XPATH, '//span[text()="注销"]'))
    # 送达管理一级菜单
    sdgl =("送达管理", (By.XPATH, '//*[@id="aside"]/ul/li[2]/div/span'))
    # 普通送达菜单
    ptsd = ("送达任务菜单按钮", (By.XPATH, '//li[contains(text(),"送达任务")]'))
