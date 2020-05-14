# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:15 
# @Author : ZHH
from selenium import webdriver
from PageObjects.ptsdList_p import PtsdList
from PageObjects.createPtsd_p import CreatePtsd
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.log import log
from PageObjects.login_p import LoginPage
import pytest
import time

@pytest.mark.usefixtures("login_success")
class TestPtsdPage:
    @pytest.mark.usefixtures("back_page")
    def test_clickNewPtsd(self, login_success):
        log.info("**********普通送达列表：正常场景   -   点击新建普通送达打开对应页面**********")
        PtsdList(login_success).new_ptsd()
        assert CreatePtsd(login_success).is_Exist_baseinfo()

    def test_no_select_down_re(self, login_success):
        log.info("**********普通送达列表：异常场景   -   不勾选工单点击下载回证，弹出提示**********")
        PtsdList(login_success).click_down_re()
        assert PtsdList(login_success).is_exist_downRe_error()
        PtsdList(login_success).click_downRe_errorOk()

    def test_export_ptsd(self,login_success):
        a = PtsdList(login_success).count_downloadsFiles()
        PtsdList(login_success).click_export_ptsd()
        time.sleep(5)
        b = PtsdList(login_success).count_downloadsFiles()
        assert a != b

