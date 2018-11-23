# coding:utf-8
import unittest
import requests
from util.log import get_logger
import datetime
from api_config.obj_factory import obj_factory
import json


class MobileLoginCase(unittest.TestCase):
    """xpos手机号码登陆测试用例"""

    @classmethod
    def setUpClass(cls):
        # 测试数据准备
        cls.request_msg = obj_factory('xpos', 'mobile_login')
        cls.request_msg.header.setdefault('token', '')
        # file_path = os.path.join(config_cls.folder_logs, f'{datetime.datetime.now().strftime("%y%m%d")}.log')
        file_path = f'{datetime.datetime.now().strftime("%y%m%d")}.log'
        cls.logger = get_logger(file_path=file_path)

    def test_01(self):
        """正确的参数"""
        self.request_msg.body = {
            'imeiCode': '',             # posimei
            'mobile': '',               # 电话号码
            'verify': '',               # 验证码
            'ip': '',                   # pos机ip地址
            'posVersion': '',           # pos机版本号
            'loginType': '',            # 登陆类型
        }
        res = requests.post(
            url=self.request_msg.url,
            headers=self.request_msg.header,
            json=self.request_msg.body,
            timeout=5
        )
        self.logger.info(
            '\n'
            f'接口的请求地址：{self.request_msg.url} \n'
            f'接口请求头部：{self.request_msg.header} \n'
            f'接口请求参数：{self.request_msg.body} \n'
            f'接口返回报文：{res.text} \n'
        )
        res_json = json.loads(res.text)
        self.assertEqual(res_json['status'], 200)



