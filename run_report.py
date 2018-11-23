import os
import unittest
from BeautifulReport import BeautifulReport
from util import HTMLTestRunner, util
import datetime
import configparser
from config import setting


# 项目根路径
BASE_PATH = os.path.dirname(__file__)


class RunReport:
    """
    输出报告
    """
    def __init__(self, config_cls):
        # 读取配置文件，创建log，reports文件夹

        folder_list = [
            os.path.join(BASE_PATH, config_cls.folder_logs),
            os.path.join(BASE_PATH, config_cls.folder_reports)
        ]

        for folder in folder_list:
            path = os.path.join(BASE_PATH, folder)
            if not os.path.isdir(path):
                os.mkdir(path)

    def add_cases(self, case_folder):
        """
        批量添加测试用例
        :case_folder:  测试用例文件夹名称
        :pattern:测试用例脚本模板
        :top_level_dir:顶层目录的名称,默认None
        :return:
        """
        case_path = os.path.join(BASE_PATH, 'testcase', case_folder)
        discover = unittest.defaultTestLoader.discover(case_path, pattern="*_case.py",
                                                       top_level_dir=None)
        # print(discover)
        return discover

    def run_cases_by_html(self, cases):
        """
        借用hmtlrunner模板输出测试用例报告
        :param cases:测试用例集
        :return:
        """

        # 格式化输出报告

        date = datetime.datetime.now().strftime('%y-%m-%d')
        file_path = os.path.join(BASE_PATH, 'reports', f'{date}_report.html')
        print('file_path:' + file_path)
        with open(file_path, 'wb') as ftp:
            # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
            runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='%s接口测试报告' % date, description='')
        runner.run(cases)

    def run_cases_by_beautiful_report(self, cases):
        """
        借用BeautifulReport模版输出测试用例报告
        :param cases:测试用例集
        :return:
        """
        report_path = os.path.join(BASE_PATH, 'reports')
        print('report_path:' + report_path)
        result = BeautifulReport(cases)
        result.report(description='测试报告', log_path=report_path)


if __name__ == "__main__":
    # print(RunReport().case_path)
    # 用例集合
    run = RunReport(setting['setting'])
    cases = run.add_cases(case_folder='xpos')
    # RunReport().run_cases_by_HTML(cases)
    run.run_cases_by_beautiful_report(cases)
