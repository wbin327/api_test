## 本人搭建的接口测试框架

### api_config模块配置了请求的基本信息
 - 我这里将一个请求抽象成一个对象，一个请求对象包含了请求头，请求路径，请求内容
 - api_config/obj_facotry.py里有一个工厂函数，传入参数构造相应的请求对象

### reports文件夹用于存放生成的测试报告

### logs文件夹用于保存日志

### util存放一些工具类

### testcase存放所有的接口测试用例

### run_report.py，程序执行的入口
