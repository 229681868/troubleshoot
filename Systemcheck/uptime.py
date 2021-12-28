#!/usr/bin/env python3
# coding: utf-8
# 测试负载情况
import os


def load_avg():
    f = os.popen("uptime | sed 's/,//g'")      # 负载统计,运行时间
    print("This cmd is uptime:")
    return f.read().strip()


def main():
    print("-------------------------测试负载情况-------------------------------")
    print(load_avg())
    print("------------------------------------------------------------------")


if __name__ == "__main__":
    main()
