# coding:utf-8


class BaseConfig(object):
    folder_logs = 'logs'
    folder_reports = 'reports'
    email_config = {
        'host': 'smtp.qq.com',
        'port': 465,
        'user': '@qq.com',
        'password': '',
        'sender': '@qq.com',
        'receive': []
    }


class TestConfig(BaseConfig):
    db_host = ''
    db_port = 3306
    db_user = 'read'
    db_password = ''
    db_database = ''
    ip = ''


class UatConfig(BaseConfig):
    db_host = ''
    db_port = 3306
    db_user = 'read'
    db_password = ''
    db_database = ''
    ip = ''


setting = TestConfig()
