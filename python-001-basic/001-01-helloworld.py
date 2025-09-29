"""
    搭建python环境
        1.下载python https://www.python.org/ftp/python/
        2.安装python
        3.配置python环境变量、Scripts环境变量(pip等命令在Scripts目录下)
        4.设置pip使用国内镜像源
            pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
            pip config set install.trusted-host mirrors.aliyun.com
            pip config list # 查看pip配置

    python helloworld 案例
"""

print("hello world!")