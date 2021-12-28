#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
from psutil._common import bytes2human


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def main():
    print("-------------------------测试内存情况-------------------------------")
    print('MEMORY\n------')
    pprint_ntuple(psutil.virtual_memory())
    print('\nSWAP\n----')
    pprint_ntuple(psutil.swap_memory())
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
