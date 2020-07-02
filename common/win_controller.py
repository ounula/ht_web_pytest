# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from pywinauto.application import Application
from common.log import log
from common.config import MicroSip_dir
from time import sleep
from pywinauto.keyboard import send_keys
import pywinauto


class WinControl:
    @staticmethod
    def upload_file(file_path, file, doc='', *args):
        try:
            # 选择文件
            app = pywinauto.Desktop()
            dlg = app["打开"]
            dlg["Toolbar3"].click()
            send_keys(file_path)
            send_keys("{VK_RETURN}")
            dlg["文件名(&N):Edit"].type_keys('"{}"'.format(file))
            for i in args:
                send_keys('"{}"'.format(i))
            dlg["打开(&O)"].click()
            log.info(doc + "上传文件成功")
        except Exception as e:
            log.error(doc + "上传文件失败")
            raise e


class MicroSIP:
    # 软电话控制，先关闭软电话检查更新
    def __init__(self, path=None, process=None):
        if path:
            try:
                self.app = pywinauto.Application(backend="uia").start(path)
                self.app2 = pywinauto.Application(backend="uia").connect(path=path)
                log.info("软电话启动成功")
            except Exception as e:
                log.error("软电话启动失败")
                raise e
        else:
            try:
                self.app = pywinauto.Application(backend="uia").connect(process=process)
                log.info("软电话程序连接成功")
            except Exception as e:
                log.error("软电话程序连接失败")
                raise e

    def open_software(self, software_path, doc=""):
        try:
            # 启动软件
            self.app = Application('uia').start(software_path)
            sleep(2)
            app2 = Application('uia').connect(path=software_path)
            dlg = app2['MicroSIP']
            log.info(doc + "开启成功")
        except Exception as e:
            log.error(doc + "开启失败")
            raise e

# app = Application('uia').start(MicroSip_dir)
# sleep(2)
# app2 = Application('uia').connect(path=MicroSip_dir)
# dlg = app2['MicroSIP']
# combox_1 = dlg['ComboBox']
# edit = combox_1.child_window(auto_id="1001", control_type="Edit")
# #截图需安装pillow
# pic = dlg.capture_as_image()
# # pic.save('01.png')
# Log().log_info("开启成功")
