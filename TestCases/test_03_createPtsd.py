# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/16 0:41
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.log import log
import pytest


class TestPtsdPage:
    @pytest.mark.usefixtures("get_ptsd_page")
    def test_createPtsd_success(self,get_ptsd_page):
        assert 1==1

