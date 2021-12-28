#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install ntplib
import ntplib
import time
import socket


def main():
    print("-------------------------测试ntp情况-------------------------------")
    hostname = socket.gethostname()   # 查看本地主机名
    print("Hostname is: ", hostname)
    # IP = socket.gethostbyname(hostname)
    # print("Local IP is: ", IP)
    ntp_client = ntplib.NTPClient()
    response_outside = ntp_client.request('ntp.aliyun.com').tx_time
    print('outside_time:', time.ctime(response_outside))    # ntp服务器时间
    response_inside = time.asctime()
    print('inside_time: ', response_inside)                 # 本地ntp时间
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
