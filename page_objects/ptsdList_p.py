# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from page_locators.ptsdList_locator import PtsdList as loc
from common.basepage import BasePage


class PtsdList(BasePage):
    def list_exist(self):
        doc = "普通送达列表"
        self.wait_elementsPresent(loc.ptsd_data, doc=doc)
        return self.get_elements(loc.ptsd_data, doc=doc)

    def new_ptsd(self):
        doc = "点击新建普通送达"
        self.wait_eleVisible(loc.create_ptsd, doc=doc)
        self.click_element(loc.create_ptsd, doc=doc)

    def reset_query(self):
        doc = "点击重置按钮"
        self.click_element(loc.reset_button, doc=doc)

    def click_down_re(self):
        doc = "点击下载回证"
        self.wait_eleVisible(loc.down_re, doc=doc)
        self.click_element(loc.down_re, doc=doc)

    def is_exist_downRe_error(self):
        doc = "定位下载回证失败提示"
        self.wait_eleVisible(loc.down_re_erro, doc=doc)
        return self.get_element(loc.down_re_erro, doc=doc)

    def click_downRe_errorOk(self):
        doc = "下载回证提示框点击确定"
        self.click_element(loc.down_re_erro, doc=doc)

    def click_export_ptsd(self):
        doc = "点击普通送达批量导出"
        self.click_element(loc.export_ptsd,doc=doc)
