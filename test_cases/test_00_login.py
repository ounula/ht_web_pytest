# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/4/12 0:32
import pytest
from PageObjects.index_p import IndexPage
from TestDatas import login_datas as LD
from Common.log import log

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    def test_login_user_noUser(self, access_web):
        log.info('**********登录：异常场景   -   不输入用户名**********')
        access_web[1].login(LD.no_user_data["用户名"], LD.no_user_data["密码"])
        assert access_web[1].pleaseInputUser(), LD.no_user_data["预期"]

    def test_wrong_user_passwd(self, access_web):
        log.info("**********登录：异常场景   -   账号或密码错误**********")
        access_web[1].login(LD.wrong_passwd_data["用户名"], LD.wrong_passwd_data["密码"])
        assert access_web[1].user_passwd_erro(), LD.wrong_passwd_data["预期"]

    @pytest.mark.parametrize("data", LD.no_passwd_data)
    def test_login_noExistUser_wrongPasswd(self, data, access_web):
        log.info("**********登录：异常场景   -   不填写密码、密码不足6位**********")
        access_web[1].login(data["用户名"], data["密码"])
        assert access_web[1].passwd_noSix(), data['预期']

    # 正常用例 - 登陆成功
    @pytest.mark.login
    def test_login_success(self, access_web):  # fixture函数作为参数，接收fixture返回值\
        log.info("**********登录：正常场景**********")
        access_web[1].login(LD.success_data["用户名"], LD.success_data["密码"])
        assert IndexPage(access_web[0]).isExist_logout_ele()
