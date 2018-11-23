# coding:utf-8
import configparser


class XposLogin(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        # 读取配置文件
        self.config.read(globals().get('BASE_PATH', '../config.ini'))

