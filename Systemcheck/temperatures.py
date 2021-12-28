#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试温度

from __future__ import print_function
import sys

import psutil


def main():
    print("-------------------------测试温度信息-------------------------------")
    if not hasattr(psutil, "sensors_temperatures"):
        sys.exit("platform not supported")
    temps = psutil.sensors_temperatures()
    if not temps:
        sys.exit("can't read any temperature")
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (
                entry.label or name, entry.current, entry.high,
                entry.critical))
        print()
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
