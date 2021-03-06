# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium import webdriver
from common import basepage
from page_objects.ptsdList_p import PtsdList
from page_objects.createPtsd_p import CreatePtsd
from test_datas import common_datas as CD
from test_datas import login_datas as LD
from common.log import log
from page_objects.login_p import LoginPage
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
        log.info("**********普通送达列表：正常场景   -   不勾选工单点击下载回证，弹出提示**********")
        PtsdList(login_success).click_down_re()
        assert PtsdList(login_success).is_exist_downRe_error()
        PtsdList(login_success).click_downRe_errorOk()

    def test_export_ptsd(self,login_success):
        log.info("**********普通送达列表：正常场景   -   点击批量导出，导出所有工单**********")
        after = PtsdList(login_success).count_downloadsFiles()
        PtsdList(login_success).click_export_ptsd()
        time.sleep(5)
        later = PtsdList(login_success).count_downloadsFiles()
        assert after < later

