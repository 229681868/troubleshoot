#!/usr/bin/env python3
# coding: utf-8
# 测试登入情况

from datetime import datetime

import psutil


def main():
    users = psutil.users()
    print("--------------------------------用户登入情况--------------------------------")
    for user in users:
        proc_name = psutil.Process(user.pid).name() if user.pid else ""
        templ = "%-14s %-14s %-14s %-18s %s"
        print(templ % ('用户', '终端', '终端开始时间', '(IP)', '协议'))
        print("%-12s %-10s %-10s %-14s %s" % (
            user.name,
            user.terminal or '-',
            datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"),
            "(%s)" % user.host if user.host else "",
            proc_name
        ))
    print("--------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
