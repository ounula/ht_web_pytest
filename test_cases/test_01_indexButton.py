# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium import webdriver
from page_objects.ptsdList_p import PtsdList
from page_objects.index_p import IndexPage
from common.log import log
from page_locators.index_locator import IndexLocator
import pytest


@pytest.mark.usefixtures("login_success")
class TestIndexPage:
    def test_click_into_sdrw(self, login_success):
        log.info("**********主页：正常场景   -   点击二级菜单<送达任务>进入对应页面**********")
        IndexPage(login_success).click_ptsd()
        assert PtsdList(login_success).list_exist()
