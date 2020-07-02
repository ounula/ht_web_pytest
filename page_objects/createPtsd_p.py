# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium import webdriver
from page_locators.createPtsd_locator import CreatePtsdLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class CreatePtsd(BasePage):
    def is_Exist_baseinfo(self):
        doc='案件基本信息标题是否存在'
        self.wait_eleVisible(loc.title,doc=doc)
        return self.get_element(loc.title,doc=doc)