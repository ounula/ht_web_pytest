# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:34 
# @Author : ZHH
from selenium import webdriver
from page_objects.ptsdList_p import PtsdList
from page_objects.index_p import IndexPage
from common.log import log
from page_locators.index_locator import IndexLocator
import pytest


@pytest.mark.usefixtures("login_success")
class TestIndexPage:
    def test_click_into_ptsd(self, login_success):
        log.info("**********主页：正常场景   -   点击二级菜单<送达任务>进入对应页面**********")
        IndexPage(login_success).click_ptsd()
        assert PtsdList(login_success).list_exist()
