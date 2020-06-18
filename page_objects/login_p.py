# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/4/12 0:00
from page_locators.loginpage_locator import LoginPageLocator as loc
from common.basepage import BasePage
from test_datas import login_datas as LD


class LoginPage(BasePage):
    # 登录
    def login(self, username, password):
        # 输入用户名、密码，点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text)
        self.input_text(loc.name_text, username, doc)
        self.input_text(loc.pwd_text, password, doc)
        self.click_element(loc.login_but, doc)

    def pleaseInputUser(self):
        doc = "错误提示框-请输入账号"
        self.wait_eleVisible(loc.errMSG_no_input_user, doc=doc)
        return self.get_text(loc.errMSG_no_input_user, doc=doc)

    def passwd_noSix(self):
        doc = "错误提示框-请输入密码_密码不足6位"
        self.wait_eleVisible(loc.errMSG_6passwd, doc=doc)
        return self.get_text(loc.errMSG_6passwd, doc=doc)

    def user_passwd_erro(self):
        doc = "错误提示框-账号或密码输入错误"
        self.wait_eleVisible(loc.errorMSG_error_user_passwd, doc=doc)
        return self.get_text(loc.errorMSG_error_user_passwd, doc=doc)

