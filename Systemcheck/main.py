import cpu
import disk_usage
import diskhealth
import fio
import gpu
import ifconfig
import iotop
import meminfo
import netstat
import network
import ntp
import ping
import sys
import free
import ps
import temperatures
import uptime
import who


def all_check():
    ping.main()
    ntp.main()
    free.main()
    gpu.main()
    uptime.main()
    # .....


if __name__ == "__main__":

    argv = sys.argv[1:]
    assert (len(argv) == 1)
    cmd = argv[0]

    lst = None
    cmds = {
        'all': all_check,
        'network': network.main,       # 网络速率统计
        'ifconfig': ifconfig.main,     # 网卡情况
        'ping': ping.main,             # 外网通信
        'net': network.main,           # 网络情况
        'ntp': ntp.main,               # NTP状态
        'free': free.main,             # 内存情况
        'mem': meminfo.main,           # 内存信息
        'netstat': netstat.main,       # 进程情况
        'ps': ps.main,                 # 进程信息
        'up': uptime.main,             # 测试负载情况
        'cpu': cpu.main,               # 负载情况
        'disk': diskhealth.main,       # 硬盘使用情况
        'diskusage': disk_usage.main,  # 存储各磁盘使用量情况
                                       # 可用fio.py测试磁盘iopS
        'uptime': uptime.main,         # 负载统计,运行时间
        'gpu': gpu.main,               # 负载统计,运行时间
        'tem': temperatures.main,      # 温度情况
        'io': iotop.main,              # 动态io信息
        'who': who.main                # 用户登入情况
    }
    if cmd in cmds:
        cmds[cmd]()
    else:
        print("invalid command, should be one of:", list(cmds.keys()))
