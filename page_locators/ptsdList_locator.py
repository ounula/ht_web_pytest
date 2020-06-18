# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 16:35 
# @Author : ZHH
from selenium.webdriver.common.by import By


class PtsdList:
    # 新建普通送达
    create_ptsd = ("新建普通送达按钮", (By.XPATH, '//span[contains(text(),"新建普通送达")]'))
    # 暂无数据div
    no_data_now = ("普通送达列表-暂无数据", (By.XPATH, '//div[@class="el-table__empty-block"]'))
    # 列表数据
    ptsd_data = ("普通送达列表", (By.XPATH, '//tr[@class="el-table__row"]'))
    # 下载回证
    down_re = ("下载回证按钮", (By.XPATH, '//a[text()="下载回证"]'))
    # 受送达人标题
    ssdr_titile = ("受送达人标题", (By.XPATH, '//h3[text()="受送达人信息"]'))
    # 重置按钮
    reset_button = ("重置", (By.XPATH, '//span[text()="重置"]'))
    # 新建电话通知
    new_call = ("新建电话通知", (By.XPATH, '//span[text()="重置"]'))
    # 下载回证失败
    down_re_erro = (
        "下载回证失败确定按钮",
        (By.XPATH, '//button[@class= "el-button el-button--default el-button--small el-button--primary "]'))
    # 批量导出
    export_ptsd = ("普通送达批量导出按钮", (By.XPATH, '//span[text()="批量导出"]'))
