# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium import webdriver
from page_locators.index_locator import IndexLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class IndexPage(BasePage):
    def isExist_logout_ele(self):
        doc = "主页注销按钮存在"
        self.wait_eleVisible(loc.logOut, doc=doc)
        return self.get_element(loc.logOut, doc=doc)

    def click_logout(self):
        doc = "点击注销按钮"
        self.click_element(loc.logOut, doc=doc)

    def click_ajgl(self):
        doc ="点击送达管理菜单"
        self.wait_eleVisible(loc.ptsd)
        self.click_element(loc.ptsd, doc=doc)

    def click_ptsd(self):
        doc = "点击菜单栏普通送达"
        self.wait_eleVisible(loc.ptsd)
        self.click_element(loc.ptsd, doc=doc)
