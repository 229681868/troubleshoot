#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os


def disk_health():

    # os.system('smartctl -s on -a /dev/disk1s1s1')
    df = os.system('df -h|head')
    select = input("请输入你要选择查看健康状态，比如格式为 '/dev/disk1s1s1' 的这个磁盘：")
    a = os.popen('sudo smartctl -s on -a %s' % select)
    b = "PASSED"
    for temp in a.readlines():
        # print(temp)
        if b in temp:
            print('This disk is ok')
            break

def main():
    print("-------------------------测试磁盘健康-------------------------------")
    disk_health()
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
