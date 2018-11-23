# coding:utf-8
import unittest
import requests
from util.log import get_logger
import datetime
import json
from api_config.obj_factory import obj_factory


class SearchOrderlistCase(unittest.TestCase):
    """获取店员销售商品订单列表测试用例,该接口必须携带token"""

    @classmethod
    def setUpClass(cls):
        # 测试数据准备
        cls.request_msg = obj_factory('xpos', 'search_order_list')
        cls.request_msg.header.setdefault('token', '')
        # file_path = os.path.join(config_cls.folder_logs, f'{datetime.datetime.now().strftime("%y%m%d")}.log')
        file_path = f'{datetime.datetime.now().strftime("%y%m%d")}.log'
        cls.logger = get_logger(file_path=file_path)

    def test_01(self):
        """正确的参数"""
        self.request_msg.body = {
            "dtBegin": '',              # 统计开始时间
            "dtEnd": '',                # 统计结束时间
            "pageIndex": '',            # 当前页码，默认第一页
            "pageSize": '',             # 每页显示长度，默认20
            "type": '',                 # -1查询所有消费订单，0查询现金收银消费订单，1查询数字货币收银消费订单
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
        self.assertEqual(res_json['code'], 200)