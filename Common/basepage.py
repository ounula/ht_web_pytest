# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:15 
# @Author : ZHH
import os
import time
import win32con
import win32gui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common import config
from Common.log import log


# 封装基本函数 - 执行日志、异常处理、失败截图
# 所有页面公共的部分
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc=""):
        """'
        :param locator: 元素定位，元祖形式
        :param wait_times: 最长等待时间
        :param poll_frequency: 轮询间隔
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            # 开始等待时间
            start = time.time()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located((locator[1])))
            # 结束等待的时间点
            end = time.time()
            # 求差值
            wait_time = round(end - start, 3)
            log.info("等待" + '"' + locator[0] + '"加载成功，用时{}秒'.format(wait_time))
        except Exception as e:
            log.error("页面加载超时！判断依据:" + '"' + locator[0] + '"')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 等待元素存在
    def wait_elePresent(self, locator, wait_times=20, poll_frequency=0.5, doc=""):
        """

        :param locator: 元素定位，元祖形式
        :param wait_times: 最长等待时间
        :param poll_frequency: 轮询间隔
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            # 开始等待时间
            start = time.time()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.presence_of_element_located((locator[1])))
            # 结束等待的时间点
            end = time.time()
            # 求差值
            wait_time = round(end - start, 3)
            log.info("等待" + '"' + locator[0] + '"加载成功，用时{}秒'.format(wait_time))
        except Exception as e:
            log.error("页面加载超时！判断依据:" + '"' + locator[0] + '"')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 等待元素元祖存在
    def wait_elementsPresent(self, locator, wait_times=20, poll_frequency=0.5, doc=""):
        """

        :param wait_times:
        :param locator: 元素定位，元祖形式
        :param wait_times 最长等待时间
        :param poll_frequency: 轮询间隔
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            # 开始等待时间
            start = time.time()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(
                EC.presence_of_all_elements_located((locator[1])))
            # 结束等待的时间点
            end = time.time()
            # 求差值
            wait_time = round(end - start, 3)
            log.info("等待" + '"' + locator[0] + '"加载成功，用时{}秒'.format(wait_time))
        except Exception as e:
            log.error("页面加载超时！判断依据:" + '"' + locator[0] + '"')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 查找元素
    def get_element(self, locator, doc=""):
        """
        :param locator: 元素定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            # 开始等待时间
            ele = self.driver.find_element(*locator[1])
            log.info("定位" + '"' + locator[0] + '"成功')
            return ele
        except Exception as e:
            log.error("定位" + '"' + locator[0] + '"失败')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 查找元素元祖
    def get_elements(self, locator, doc=""):
        """
        :param locator: 元素定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            ele = self.driver.find_elements(*locator[1])
            log.info("定位" + '"' + locator[0] + '"成功')
            return ele
        except Exception as e:
            log.error("定位" + '"' + locator[0] + '"失败')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 点击操作
    def click_element(self, locator, doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            ele.click()
            log.info("点击：{0}".format(locator[0]))
        except Exception as e:
            log.error("点击" + locator[0] + "失败！")
            #  截图
            self.save_screenshot(doc)
            raise e

    # 输入操作
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            ele.send_keys(text)
            log.info('向"' + locator[0] + '"输入内容:{}'.format(text))
        except Exception as e:
            log.error('向"' + locator[0] + '"输入内容:{}失败！'.format(text))
            #  截图
            self.save_screenshot(doc)
            raise e

    # 清空输入内容
    def clear_text(self, locator, doc=""):
        try:
            ele = self.get_element(locator)
            ele.clear()
            log.info('清空"' + locator[0] + '"文本')
        except Exception as e:
            log.error('清空"' + locator[0] + '"文本失败！')
            self.save_screenshot(doc)
            raise e

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        try:
            ele = self.get_element(locator, doc=doc)
            text = ele.text
            log.info('获取"' + locator[0] + '"文本，内容为:{}'.format(text))
            return text
        except Exception as e:
            log.error('获取"' + locator[0] + '"文本内容失败！')
            #  截图
            self.save_screenshot(doc)
            raise e

    # 获取元素属性
    def get_element_attribute(self, locator, attr, doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            return ele.get_attribute(attr)
        except Exception as e:
            log.error("获取元素属性失败！定位:{}".format(locator))
            #  截图
            self.save_screenshot(doc)
            raise e

    # alert处理
    def alert_action(self, action="accept"):
        pass

    # 谷歌上传文书
    def upload_file(self, file_path, doc):
        time.sleep(2)
        try:
            # 一级窗口（打开）
            open_win = win32gui.FindWindow("#32770", "打开")
            # 二级窗口
            combo_box_ex32 = win32gui.FindWindowEx(open_win, 0, "ComboBoxEx32", None)
            # 三级窗口
            combo_box = win32gui.FindWindowEx(combo_box_ex32, 0, "ComboBox", None)
            # 四级窗口（文件名）
            edit = win32gui.FindWindowEx(combo_box, 0, "Edit", None)
            # 二级窗口（打开）
            button = win32gui.FindWindowEx(open_win, 0, "Button", "打开(&O)")
            # 操作
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
            time.sleep(1)
            win32gui.SendMessage(open_win, win32con.WM_COMMAND, 1, button)
            log.info("上传本地文书：{}".format(file_path))
        except Exception as e:
            log.error("上传文书失败！路径:{}".format(file_path))
            self.save_screenshot(doc)
            raise e

    # 滚动条处理（移动到元素顶部和当前窗口顶端对齐）
    def scroll_to_element(self, locator, doc=""):
        log.info("开始滚动条处理，拖动位置:{}".format(locator[0]))
        try:
            # 开始等待时间
            start = time.time()
            ele = self.get_element(locator, doc=doc)
            # 结束等待的时间点
            end = time.time()
            # 求差值
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            wait_time = round(end - start, 3)
            log.info("滚动条处理成功，用时{}秒".format(wait_time))
            time.sleep(1)
        except Exception as e:
            log.error("滚动条处理失败，定位：{}".format(locator))
            self.save_screenshot(doc)
            raise e

    # 取消read-only属性
    def do_js(self, locator, doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', ele)
            log.info('去除"' + locator[0] + '"只读属性')
        except Exception as e:
            log.error('去除"' + locator[0] + '"只读属性失败！')
            raise e

    # 窗口切换

    # 统计下载文件夹内文件数量
    @staticmethod
    def count_downloadsFiles():
        try:
            count = len(os.listdir(config.downloads_dir))
            log.info("获取下载目录文件数：{}".format(count))
            return count
        except Exception as e:
            log.error("获取下载目录文件失败")
            raise e

    # 截图
    def save_screenshot(self, doc=""):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        file_path = config.screenshot_dir + \
                   "\\{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S"))
        try:
            self.driver.save_screenshot(file_path)
            log.info("截屏成功，图片路径为{}".format(file_path))
        except Exception as e:
            log.error("截图失败")
            raise e
