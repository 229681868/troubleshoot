import json
import logging
import os

from fabric.api import env, run, sudo, reboot, settings, parallel, local, put
logging.basicConfig(level=logging.INFO)
env.user = 'ps'
env.password = '6block'


def get_hosts():
    hosts = []
    #hosts.extend(get_part(part_name='storage'))
    # hosts.extend(get_part(part_name='computing'))
    # hosts = hosts[:1]
    logging.info("%s %s" % (hosts, len(hosts)))
    cmd = 'lotus-miner storage list|grep lotusminer|awk -F"Local:" \"{0}\"|cut -d "/" -f3'.format("{print $2}")
    #hosts = os.popen(cmd).read().strip().split("\n")
    hosts = os.popen(cmd).readlines()
    return hosts


env.hosts = get_hosts()


@parallel(1)
def hello():
    run('df -H')
    #sudo('lsblk -Jp |grep "/dev/sd*"')


@parallel
def time_adjust():
    sudo('ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime')
    sudo('ntpdate ntp.aliyun.com')



@parallel(1)
def iperf():
    # ip = local('hostname -I', capture=True).split(' ')[1]
    ip = local('hostname -I', capture=True)
    run('iperf -t 1 -c %s' % ip)


@parallel
def clear():
    sudo('sed -i "/mnt\/disk/d" /etc/fstab')
    sudo('sed -i "/#/!d" /etc/exports')


@parallel
def add_ssh_key():
    ssh_key = local('cat /home/ps/.ssh/id_rsa.pub', capture=True)
    run('mkdir -p /home/ps/.ssh')
    run('touch /home/ps/.ssh/authorized_keys')
    run('sed -i "/filecoin-main/d" /home/ps/.ssh/authorized_keys')
    run('echo "%s" >> /home/ps/.ssh/authorized_keys' % ssh_key)


@parallel
def time_adjust():
    sudo('ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime')
    sudo('ntpdate -t 5 ntp.aliyun.com')


@parallel(1)
def lsblk():
    run('lsblk | grep T')

@parallel
def iperf_receiving():
    run('iperf -s')

@parallel
def one_key():
    add_ssh_key()
    time_adjust()
    iperf()

