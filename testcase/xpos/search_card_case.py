# coding:utf-8
import unittest
from api_config.xpos.search_card_config import SearchCardConfig
import requests
from util.log import get_logger
from config import setting
import os
import datetime
import json


class SearchCardCase(unittest.TestCase):
    """查卡2.卡片校验"""

    @classmethod
    def setUpClass(cls):
        # 测试数据准备
        config_cls = setting['config']
        cls.api_config_cls = SearchCardConfig()
        cls.post_header = {}
        cls.post_data = {}
        cls.post_header.setdefault('Content-Type', 'application/json')
        cls.post_header.setdefault('token', '')
        cls.url = f'{config_cls.ip}{cls.api_config_cls.url}'
        # file_path = os.path.join(config_cls.folder_logs, f'{datetime.datetime.now().strftime("%y%m%d")}.log')
        file_path = f'{datetime.datetime.now().strftime("%y%m%d")}.log'
        cls.logger = get_logger(file_path=file_path)

    def test_01(self):
        """正确的参数"""
        res = requests.post(url=self.url, headers=self.post_header, json=self.api_config_cls.request_param['success'],
                            timeout=5)
        self.logger.info('接口的请求地址：%s' % self.url)
        self.logger.info('接口请求头部：%s' % self.post_header)
        self.logger.info('接口请求参数：%s' % self.api_config_cls.request_param['success'])
        self.logger.info('接口返回报文：%s' % res.text)
        res_json = json.loads(res.text)
        self.assertEqual(res_json['code'], 200)