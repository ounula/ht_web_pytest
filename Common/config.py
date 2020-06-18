# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 13:55 
# @Author : ZHH
import os
from Common.get_conf import MyConf

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试数据
testdatas_dir = os.path.join(base_dir, "TestDatas")

# 测试用例
testcase_dir = os.path.join(base_dir, "TestCases")

# 配置文件
conf_dir = os.path.join(base_dir, "Config")

# 软电话目录
MicroSip_dir = r'C:\Users\yiii\AppData\Local\MicroSIP\microsip.exe'

# html报告
htmlreport_dir = os.path.join(base_dir, "Outputs\\reports")

# 日志文件
logs_dir = os.path.join(base_dir, "Outputs\\logs")

# 截图
screenshot_dir = os.path.join(base_dir, "Outputs\\screenshots")

# 下载文件
downloads_dir = os.path.join(base_dir, "Outputs\\downloads")

# 获取配置文件的绝对路径
conf_path = os.path.join(conf_dir, "conf.ini")
conf = MyConf(conf_path)
