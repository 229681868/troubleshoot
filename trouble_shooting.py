#!/usr/bin/python3.6

import worker_phase_status
import miner_status
import sys

red_head = "\033[1;31;40m"
red_tail = "\033[0m"
col_head = "\033[1;36;1m"
col_tail = "\033[0m"

def all_worker_status():
    worker = worker_phase_status.Worker()
    workers = worker.get_workers()
    for ip in workers:
        print("{0}IP:{1}".format(col_head, col_tail) + ip)
        p1_status = worker.get_p1_status("seal_pre_commit_phase1", ip)
        p2_status = worker.get_p2_status("seal_pre_commit_phase2", ip)
        c2_status = worker.get_c2_status("seal_commit_phase2", ip)

        if p1_status:
            print("{0}P1:{1}".format(col_head, col_tail) + str(p1_status))
        if p2_status:
            print("{0}P2:{1}".format(col_head, col_tail) + str(p2_status))
        if c2_status:
            print("{0}C2:{1}".format(col_head, col_tail) + str(c2_status))

        print(str(worker.get_seal_num("seal_commit_phase2", ip)) + "{0} power/day {1}".format(col_head, col_tail))
        print("----------------------------------------------------------")


def worker_status(ip):
    worker = worker_phase_status.Worker()
    print("{0}IP:{1}".format(col_head, col_tail) + ip)
    p1_status = worker.get_p1_status("seal_pre_commit_phase1", ip)
    p2_status = worker.get_p2_status("seal_pre_commit_phase2", ip)
    c2_status = worker.get_c2_status("seal_commit_phase2", ip)

    if p1_status:
        print("{0}P1:{1}".format(col_head, col_tail) + str(p1_status))
    if p2_status:
        print("{0}P2:{1}".format(col_head, col_tail) + str(p2_status))
    if c2_status:
        print("{0}C2:{1}".format(col_head, col_tail) + str(c2_status))
    print(str(worker.get_seal_num("seal_commit_phase2", ip)) + "{0} power/day {1}".format(col_head, col_tail))
    print("----------------------------------------------------------")

def check_worker(ip):
    worker = worker_phase_status.Worker()
    print("{0}Worker GPU INFO:{1}".format(col_head, col_tail))
    worker.check_worker_gpu(ip)
    print("{0}Worker DISK INFO:{1}".format(col_head, col_tail))
    worker.check_worker_disk(ip)
    print("{0}Worker Log:{1}".format(col_head, col_tail))
    worker.get_worker_log(ip)

def miner_disk_status():
    miner = miner_status.Miner()
    miner_disk_info = miner.miner_disk_status()
    if miner_disk_info != "":
        print("{0}Miner Disk status:{1}".format(col_head, col_tail) + miner_disk_info)

def miner_gpu_status():
    miner = miner_status.Miner()
    print("{0}Miner Gpu status:{1}".format(col_head, col_tail) + miner.miner_gpu_status())

def minerTostorage_network():
    miner =  miner_status.Miner()
    miner.minerTostorage_network()


def miner_sync_staus():
    miner =  miner_status.Miner()
    miner.miner_sync_staus()

def winning_block(day):
    miner = miner_status.Miner()
    print("{0}winning nums:{1}".format(col_head, col_tail) + str(miner.winning_block(day)))

def lost_sectors_info():
    miner = miner_status.Miner()
    lost_sectors_info = miner.lost_sectors_info()
    if lost_sectors_info != "":
        print("{0}lost power info:{1}".format(red_head, red_tail) + lost_sectors_info)

def help_info():
    help_info = "lack of parameter example for {0} <parameter>\n\
                all_worker_status\n\n\
                worker_status <host_ip>\n\n\
                check_worker\n\n\
                miner_disk_status\n\n\
                miner_gpu_status\n\n\
                storage_network\n\n\
                winning_block <day>\n\n\
                lost_sectors\n\n\
                quickly_check".format(sys.argv[0])
    print(help_info)

if __name__ == '__main__':
    result = ""
    result = sys.argv[1:]
    try:
        if result[0] == "" or result[0] == "help":
            help_info()
            exit(0)
        elif result[0] == "all_worker_status":
            all_worker_status()
        elif result[0] == "worker_status":
            worker_status(result[1])
        elif result[0] == "check_worker":
            check_worker(result[1])
        elif result[0] == "miner_disk_status":
            miner_disk_status()
        elif result[0] == "miner_gpu_status":
            miner_gpu_status()
        elif result[0] == "storage_network":
            minerTostorage_network()
        elif result[0] == "winning_block":
            winning_block(result[1])
        elif result[0] == "lost_sectors":
            lost_sectors_info()
        elif result[0] == "quickly_check":
            miner_disk_status()
            miner_gpu_status()
            minerTostorage_network()
            lost_sectors_info()
            miner_sync_staus()
        else:
            help_info()
            exit(0)

    except IndexError:
            help_info()
            exit(0)
