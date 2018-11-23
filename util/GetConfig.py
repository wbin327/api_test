import configparser
import os


class GetConfig(object):
    """
    读取环境设置
    """

    def __init__(self, path='../api_config/api_config.ini'):
        self.config = configparser.ConfigParser()
        # self.path = os.path.dirname(__file__) + path  # 配置文件路径
        self.path = path

    def get_config(self, title, subtitle):
        """
        :param title: 配置头部
        :param subtitle: 配置内的内容
        :return:
        """

        if not os.path.isfile(self.path):
            raise Exception('api_config.ini not found,配置文件不存在')
        self.config.read(self.path)  # 读取配置文件
        if title not in self.config.sections():
            raise Exception(f'element not found, 查找不到元素{title}')
        elif subtitle not in self.config.options(title):
            raise Exception(f'element not found, 查找不到元素{subtitle}')
        else:
            setting = self.config.get(title, subtitle)
        return setting
