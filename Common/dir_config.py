# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 13:55 
# @Author : ZHH
import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcase_dir = os.path.join(base_dir,"TestCases")

htmlreport_dir = os.path.join(base_dir,"Outputs/reports")

logs_dir = os.path.join(base_dir,"Outputs/logs")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")

downloads_dir = os.path.join(base_dir,"Outputs/downloads")

downloads_dir = os.path.join(base_dir,"Outputs/downloads")

conf_dir = os.path.join(base_dir,"Config")

#软电话目录
MicroSip_dir =r'C:\Users\yiii\AppData\Local\MicroSIP\microsip.exe'