# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19

# 正常场景
success_data = {"用户名": "zhh", "密码": "123456"}

# 异常场景   -   不填写用户名
no_user_data = {"用户名": "", "密码": "python", "预期": "请输入账号"}

# 异常场景   -   不填写密码、密码不足6位
no_passwd_data = [
    {"用户名": "zhuhonghao", "密码": "", "预期": "请输入密码"},
    {"用户名": "dsadsadsa", "密码": "pytho", "预期": "请输入至少6位数的密码"}
]

# 异常场景   -   账号或密码错误
wrong_passwd_data = {"用户名": "18684720553", "密码": "python321", "预期": "登录错误，请检查用户名或密码是否正确!"}
