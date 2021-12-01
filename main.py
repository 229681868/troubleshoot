#!/usr/bin/python
import os
import re
import datetime

def get_workers():
    try:
        workers = os.popen('lotus-miner sealing workers|\
                        grep -e "[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+"|\
                        cut -d" " -f4').read()
        workers = list(re.sub(":[0-9]+", "", workers).strip().split("\n"))
    except IndexError:
        print("not worker running")
    return workers


def format_str(or_str):
    index1 = or_str.find("[20")
    index2 = or_str.find("][INFO]")
    or_str = or_str[index1:index2].replace("[", "").replace("]", " ")
    or_str = re.sub("\.[0-9]+", "", or_str)
    return or_str


def get_spent_time(or_time1, or_time2):
    t1 = datetime.datetime.strptime(or_time1, '%Y-%m-%d %H:%M:%S')
    t2 = datetime.datetime.strptime(or_time2, '%Y-%m-%d %H:%M:%S')
    spent_time = t2 - t1
    return spent_time


def get_p1_status(phase, date1, date2, host_ip):
    cmd = "cat ~/share/hdd/log/worker.{4}.log|\
         grep {0}|egrep \"{1}|{2}\"|\
         grep SectorId|sort -k 3|\
         awk '/start/,/finish/{3}'".format(phase, date1, date2, "{print}", host_ip)

    p1 = os.popen(cmd).read().strip().split("\n")
    map = {}
    l1 = []
    l2 = []
    try:
        for i in range(0, 10):
            str1 = p1[i]
            if str1.find("start") > 0:
                l1.append(p1[i])
            else:
                l2.append(p1[i])

        for v in range(0, len(l1)):
            p1_str1 = l1[v]
            p1_str2 = l2[v]
            str1 = format_str(p1_str1)
            str2 = format_str(p1_str2)
            spent_time = get_spent_time(str1, str2)
            map[p1_str1[p1_str1.find("SectorId"):]] = str(spent_time)
    except IndexError:
        print("not seal_pre_commit_phase1 log")

    return map


def get_p2_status(phase, date1, date2, host_ip):
    cmd = "cat ~/share/hdd/log/worker.{3}.log| \
        grep {0}| \
        egrep \"{1}|{2}\"".format(phase, date1, date2, host_ip)
    p2 = os.popen(cmd).read().strip().split("\n")
    p2_list1 = []
    p2_list2 = []
    spent_time_list = []
    try:
        for i in range(0, len(p2)):
            if i == 0 and p2[i].find("finish") > 0: p2.remove(p2[i])
            if i == 1 and p2[i].find("finish") > 0: p2.remove(p2[i])
            if i <= 19 and i % 2 != 0:
                if p2[i].find("start") > 0:
                    p2_list1.append(p2[i])
                else:
                    p2_list2.append(p2[i])

        for v in range(0, len(p2_list1)):
            p2_str1 = p2_list1[v]
            p2_str2 = p2_list2[v]
            or_time1 = format_str(p2_str1)
            or_time2 = format_str(p2_str2)
            spent_time = get_spent_time(or_time1, or_time2)
            spent_time_list.append(str(spent_time))
    except IndexError:
        print("not seal_pre_commit_phase2 log")

    return spent_time_list


def get_c2_status(phase, date1, date2, host_ip):
    cmd = "cat ~/share/hdd/log/worker.{3}.log|\
           grep {0}|\
           egrep \"{1}|{2}\"|\
           grep SectorId".format(phase, date1, date2, host_ip)

    c2 = os.popen(cmd).read().strip().split("\n")
    map = {}
    l1 = []
    l2 = []
    try:
        if c2[0].find("finish") > 0: c2.remove(c2[0])
        for i in range(0, 10):
            str1 = c2[i]
            if str1.find("start") > 0:
                l1.append(c2[i])
            else:
                l2.append(c2[i])

        for v in range(0, len(l1)):
            p1_str1 = l1[v]
            p1_str2 = l2[v]
            str1 = format_str(p1_str1)
            str2 = format_str(p1_str2)
            spent_time = get_spent_time(str1, str2)
            map[p1_str1[p1_str1.find("SectorId"):]] = str(spent_time)
    except IndexError:
        print("not seal_commit_phase2 log")

    return map


def get_seal_num(phase, date1, host_ip):
    cmd1 = "cat /home/ps/share/hdd/log/worker.{0}.log| \
           grep {1}| \
           grep \"{2}\"| \
           grep SectorId| \
           grep finish|wc -l".format(host_ip, phase, date1)

    cmd2 = "lotus-miner info --hide-sectors-info| \
            grep \"Miner:\"| \
            cut -d\" \" -f3"
    size = float(os.popen(cmd2).read().replace("(", ""))
    num = float(os.popen(cmd1).read())
    return num * size / 1024

if __name__ == '__main__':
    today = datetime.date.today()
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    workers = get_workers()

    for w in workers:
        print(w)
        #print(worker.get_p1_status("seal_pre_commit_phase1",today,yesterday,w))
        #print(worker.get_p2_status("seal_pre_commit_phase2",today,yesterday,w))
        #print(worker.get_c2_status("seal_commit_phase2",today,yesterday,w))
        #print(worker.get_seal_num("seal_commit_phase2",yesterday,w))