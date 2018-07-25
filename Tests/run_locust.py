# coding:utf-8
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Util import *
import multiprocessing


def start_slave(locust_file, master_port):
    print 'start slave pid:\t{0}'.format(os.getpid())
    os.system('locust -f {0} --slave --master-port {1}'.format(locust_file, master_port))


if __name__ == '__main__':
    multiprocessing.freeze_support()
    LU = locustUtil()
    # 读取配置config/locust.yml，生成locustfile.py
    locust_file = LU.genLocustfile()
    # 生成locust运行命令
    locust_command = LU.getRunCommand()

    # 运行locust
    if 'master' in locust_command:
        # 分布式
        num = LU.cases['params'].get('slaves_num', multiprocessing.cpu_count())
        master_port = LU.cases['params'].get('master_port', 5557)
        record = []
        for i in range(num):
            process = multiprocessing.Process(target=start_slave, args=(locust_file, master_port))
            process.start()
            record.append(process)

        print 'start master pid:\t{0}'.format(os.getpid())
        cmd = 'locust -f {0} {1}'.format(locust_file, locust_command)
        print 'cmd:\t{0}'.format(cmd)
        os.system(cmd)
    else:
        # 单例模式
        cmd = 'locust -f {0} {1}'.format(locust_file, locust_command)
        print 'cmd:\t{0}'.format(cmd)
        os.system(cmd)
