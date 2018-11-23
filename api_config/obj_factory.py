# coding:utf-8
import os, sys
import importlib
import config


def obj_factory(module_dir, api_name):
    """
    工厂函数，为基础的请求类赋值，并返回
    :param module_dir: python模块的名字
    :param api_name: 接口名称
    :param server: 有两个值test和uat，分别代表不同的服务器
    :return:
    """

    # 需要将本模块添加到sys.path中，否则会报错moduleNotFound
    package_path = os.path.dirname(__file__)
    sys.path.append(package_path)

    # 获取文件夹下所有.py模块名
    modules = get_modules(module_dir)

    body = dict()
    url = ''
    header = dict()
    for module in modules:
        module = importlib.import_module(module, f'{module_dir}')
        if getattr(module, 'url'):
            url = getattr(module, 'url')[api_name]
        if getattr(module, 'body'):
            body = getattr(module, 'body')[api_name]
        if getattr(module, 'header'):
            header = getattr(module, 'header')

    base_request = BaseRequest(url, header, body, config.setting.ip)
    return base_request


def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名,这里使用绝对路径
    """
    modules = []
    files = os.listdir(os.path.join(os.path.dirname(__file__), package))

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append("." + name)

    return modules


class BaseRequest(object):
    """基础的请求类"""

    def __init__(self, url='', header={}, body={}, ip=''):
        self.url = url
        self.header = header
        self.body = body
        self.url = f'{ip}{url}'


if __name__ == '__main__':
    obj_factory('xpos', 'add_client_mobileandemail')