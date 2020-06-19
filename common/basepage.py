# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:15 
# @Author : ZHH
import os
from selenium import webdriver
import time
import win32con
import win32gui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import config
from common.log import log


# 封装基本函数 - 执行日志、异常处理、失败截图
# 所有页面公共的部分
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        set_headless = config.conf.get_str("env", "head_less")
        set_browser = config.conf.get_str("env", "browser")
        project_url = config.conf.get_str("env", "url")
        try:
            if set_browser == "Chrome":
                options = webdriver.ChromeOptions()
                prefs = {
                    "download.prompt_for_download": False,
                    'download.default_directory': config.downloads_dir,  # 下载目录
                    'profile.default_content_settings.popups': 0,  # 设置为0，禁止弹出窗口
                    'safebrowsing.enabled': True,
                }
                options.add_experimental_option('prefs', prefs)
                if set_headless == "True":
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                self.driver = webdriver.Chrome(options=options, executable_path=config.driver_path)
                self.driver.maximize_window()
                self.driver.get(url=project_url)
                log.info(f"打开{set_browser}浏览器成功")
                return self.driver
            else:
                raise Exception("暂不支持其他浏览器")
        except Exception as e:
            log.error("拉起浏览器失败")
            raise e

    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc=""):
        """'
        等待元素可见
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

    def wait_elePresent(self, locator, wait_times=20, poll_frequency=0.5, doc=""):
        """
        等待元素存在
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

    def wait_elementsPresent(self, locator, wait_times=20, poll_frequency=0.5, doc=""):
        """
        等待元素（多个）存在
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

    def get_element(self, locator, doc=""):
        """
        查找元素
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

    def get_elements(self, locator, doc=""):
        """
        查找元素（多个）
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
        """
        点击操作
        :param locator: 元素名称
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        ele = self.get_element(locator, doc=doc)
        try:
            ele.click()
            log.info("点击：{0}".format(locator[0]))
        except Exception as e:
            log.error("点击" + locator[0] + "失败！")
            #  截图
            self.save_screenshot(doc)
            raise e

    def input_text(self, locator, text, doc=""):
        """
        输入操作
        :param locator: 元素定位
        :param text: 输入的内容
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        ele = self.get_element(locator, doc=doc)
        try:
            ele.send_keys(text)
            log.info('向"' + locator[0] + '"输入内容:{}'.format(text))
        except Exception as e:
            log.error('向"' + locator[0] + '"输入内容:{}失败！'.format(text))
            #  截图
            self.save_screenshot(doc)
            raise e

    def clear_text(self, locator, doc=""):
        """
        清空输入内容
        :param locator: 元素定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        try:
            ele = self.get_element(locator)
            ele.clear()
            log.info('清空"' + locator[0] + '"文本')
        except Exception as e:
            log.error('清空"' + locator[0] + '"文本失败！')
            self.save_screenshot(doc)
            raise e

    def get_text(self, locator, doc=""):
        """
        获取元素的文本内容
        :param locator: 元素定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
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

    def get_element_attribute(self, locator, attr, doc=""):
        """
        获取元素属性
        :param locator: 元素定位
        :param attr: 属性名称
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        ele = self.get_element(locator, doc=doc)
        try:
            return ele.get_attribute(attr)
        except Exception as e:
            log.error("获取元素属性失败！定位:{}".format(locator[0]))
            #  截图
            self.save_screenshot(doc)
            raise e

    # alert处理
    def alert_action(self, action="accept"):
        pass

    def upload_file(self, file_path, doc):
        """
        谷歌上传文件
        :param file_path: 文件地址
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
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

    def scroll_to_element(self, locator, doc=""):
        """
        滚动条处理（移动到元素顶部和当前窗口顶端对齐）
        :param locator: 元素定位
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
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
            log.error("滚动条处理失败，定位：{}".format(locator[0]))
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

    def switch_to_windows(self, locator, timeout=20, frequency=0.5):
        """
        窗口切换
        :param locator: 元素定位
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        """
        try:
            cur_handles = self.driver.window_handles  # 获取点击之前的窗口总数
            start_time = time.time()
            self.click_element(locator, doc=f"点击{locator[0]}等待窗口出现")  # 点击按钮后新的窗口出现
            log.info(f"点击{locator[0]}等待窗口出现")
            WebDriverWait(self.driver, timeout, frequency).until(EC.new_window_is_opened(cur_handles))
            wins = self.driver.window_handles  # 再次获取窗口总数
            self.driver.switch_to.window(wins[-1])  # 切换到新的页面
            end_time = time.time()
            time2 = round(end_time - start_time, 2)
            log.info("根据元素{}进行窗口切换，等待用时{}秒".format(locator[0], time2))
        except Exception as e:
            log.error("根据元素{}进行窗口切换失败！".format(locator[0]))
            raise e

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

    def save_screenshot(self, doc=""):
        """
        截图
        :param doc:
        :return:
        """
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        file_path = config.screenshot_dir + \
                    "\\{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S"))
        try:
            self.driver.save_screenshot(file_path)
            log.info("截屏成功，图片路径为{}".format(file_path))
        except Exception as e:
            log.error("截图失败")
            raise e


if __name__ == '__main__':
    BasePage(driver=1).open_browser()
