#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import subprocess


# from fabric.api import env,run,settings,parallel,local
class TimeoutError(Exception):
    pass


def gpu_status(cmd, timeout=1):
    print("The cmd is : " + cmd)
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            p.terminate()
            raise TimeoutError(cmd, timeout)
        time.sleep(0.1)
    return p.stdout.read()


def main():
    print(gpu_status(cmd='nvidia-smi', timeout=1))    # 查看显卡状态，驱动状态状态


if __name__ == '__main__':
    main()
