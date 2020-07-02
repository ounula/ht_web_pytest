# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    name_text = ("用户名输入框", (By.XPATH, '//input[@placeholder="请输入您的用户名"]'))
    # 密码输入框
    pwd_text = ("密码输入框", (By.XPATH, '//input[@placeholder="请输入您的密码"]'))
    # 登录按钮
    login_but = ("登录按钮", (By.XPATH, '//button[@class="el-button el-button--primary"]'))
    # 错误提示框-密码不足6位
    errMSG_6passwd = ("错误提示框-密码不足6位", (By.XPATH, '//div[contains(text(),"密码")]'))
    # 错误提示框-请输入账号
    errMSG_no_input_user = ("错误提示框-请输入账号", (By.XPATH, '//div[contains(text(),"请输入账号")]'))
    # 错误提示信息-账号密码错误
    errorMSG_error_user_passwd = ("错误提示框-账号密码错误", (By.XPATH, '//p[contains(text(),"用户名或密码是否正确")]'))
