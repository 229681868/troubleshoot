#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试外网是否互通

import os
import sys
import logging
import fcntl
import subprocess

LOGFILE = "./ping_outnet.log"
domain_add = ["www.baidu.com", "www.qq.com", "www.sina.com.cn", "www.1688.com", "www.taobao.com", "8.8.8.8",
              "114.114.114.114"]
pidfile = 0
i = 1


# 定义日志等级和输出信息
def log_log(level='debug', action='message'):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [PID-%(process)d] - [%(pathname)s-line:%(lineno)d] [%(levelname)s] %('
                               'message)s',
                        datefmt='%Y-%m-%d %H:%M', filename=LOGFILE, filemode='a')
    if level == 'debug':
        logging.debug(action)
    elif level == 'info':
        logging.info(action)
    elif level == 'warn':
        logging.warn(action)
    elif level == 'error':
        logging.error(action)
    else:
        logging.critical(action)


def ApplicationInstance():
    global pidfile
    pidfile = open(os.path.realpath(__file__), "r")
    try:
        fcntl.flock(pidfile, fcntl.LOCK_EX | fcntl.LOCK_NB)  # 创建一个排他锁,并且所被锁住其他进程不会阻塞
        log_log('info', 'continue...')
    except:
        log_log('error', 'The script was executed many times...')
        sys.exit(1)


def maintest():
    try:
        for domain in domain_add:
            value = os.system("ping -q -c 3 %s" % domain)
            if value != 0:
                out_print = subprocess.Popen(['ping', '-c 3', '%s' % domain], stdout=subprocess.PIPE).communicate()[0]
                log_log('warn', 'ping %s Destination Host Unreachable - %s' % (domain, value))
                log_log('debug', "connect: Network is unreachable")
                log_log('debug', out_print)
            else:
                log_log('info', 'ping %s successful' % domain)
                has_error = 0
                break
        else:
            log_log('warn', 'ping all domains Destination Host Unreachable')
            has_error = 1
    except Exception as e:
        has_error = 1
        log_log('warn', '%s - 脚本执行异常' % e)
    return has_error


def main():
    print("-------------------------测试外网通信-------------------------------")
    i = 0
    ApplicationInstance()
    has_error = maintest()
    while i < 3:
        if has_error == 1:
            has_error = maintest()
            i += 1
        else:
            break
    else:
        log_log('error', '3times ping all domains Destination Host Unreachable')
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
