# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium import webdriver
from page_objects.login_p import LoginPage
from page_objects.index_p import IndexPage
from test_datas import common_datas as CD
from test_datas import login_datas as LD
from common.log import log
import pytest


class TestPtsdPage:
    @pytest.mark.usefixtures("get_ptsd_page")
    def test_createPtsd_success(self,get_ptsd_page):
        assert 1==1

