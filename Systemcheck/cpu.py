#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 前三个是1、5、15分钟内的平均进程数。第四个的分子是正在运行的进程数，分母是进程总数；最后一个最近运行的进程ID号
def load_stat():
    loadavg = {}
    try:
        f = open("/proc/loadavg")
        con = f.read().split()
        f.close()
        loadavg['lavg_1'] = con[0]
        loadavg['lavg_5'] = con[1]
        loadavg['lavg_15'] = con[2]
        loadavg['nr'] = con[3]
        loadavg['last_pid'] = con[4]
    except Exception as e:
        print("不存在/proc/loadavg文件，查看负载失败")
    return loadavg


def main():
    load_stat()
    print("1min overload", load_stat()['lavg_1'])
    print("5min overload", load_stat()['lavg_5'])
    print("15min overload", load_stat()['lavg_15'])
    print("Number of processes", load_stat()['nr'])
    print("Last Process ID number", load_stat()['last_pid'])


if __name__ == '__main__':
    main()
