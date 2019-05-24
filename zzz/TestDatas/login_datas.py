#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 14:48

#正常场景 -- 登陆成功的测试数据;
login_succs = {"username":"18684720553",
               "passwd":"python",
               "check":"我的帐户[小小蜂96027]"}

#异常场景  - 无用户名、无密码、手机号格式 不正确
login_noData = [
    {"username":"","passwd":"python","check":"请输入手机号"},
    {"username":"18684720553","passwd":"","check":"请输入密码"},
    {"username":"186847208","passwd":"python","check":"请输入正确的手机号"}
]

#异常的场景  - 错误的密码、账号未注册没有授权 。
wrong_data = [
    {"user":"18684720553","passwd":"python111","check":"帐号或密码错误!"},
    {"user":"18600001100","passwd":"python","check":"此账号没有经过授权，请联系管理员!"}
]