# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium.webdriver.common.by import By


class CreatePtsdLocator:
    # 案件基本信息标题
    title = ("案件基本信息标题", (By.XPATH, '//h3[text()="案件基本信息"]'))
    # 案号年份
    ah_year = ("年份选择框", (By.XPATH, '//input[contains(@placeholder,"请选择年份")]'))
    # 选择年份
    year_2020 = ("年份选择2020年", (By.XPATH, '//span[text()=2020]'))
    # 法院代字
    ah_daizi = ("法院代字选择框", (By.XPATH, '//input[@placeholder="请选择法院代字"]'))
    # 常用代字
    daizi_cy = ("常用代字按钮", (By.XPATH, '//div[@aria-controls="pane-0"]'))
    # 非常用类型代字
    daizi_no_cy = ("非常用代字按钮", (By.XPATH, '//div[@aria-controls="pane-1"]'))
    # 自定义代字
    daizi_define = ("自定义代字按钮", (By.XPATH, '//div[@aria-controls="pane-2"]'))
    # 请输入自定义按键类型代字
    daizi_define_input = ("自定义代字输入框", (By.XPATH, '//input[contains(@placeholder,"请输入自定义")]'))
    # 案由
    ay = ("案由输入框", (By.XPATH, '//input[@placeholder="请输入案由"]'))
