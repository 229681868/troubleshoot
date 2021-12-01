#!/usr/bin/python3.6
import worker_phase_status
import sys

def get_worker_status():
    worker = worker_phase_status.Worker()
    workers = worker.get_workers()
    for ip in workers:
        print(ip)
        print(worker.get_p1_status("seal_pre_commit_phase1", ip))
        print(worker.get_p2_status("seal_pre_commit_phase2", ip))
        print(worker.get_c2_status("seal_commit_phase2", ip))
        print(worker.get_seal_num("seal_commit_phase2", ip))


if __name__ == '__main__':
    result=""
    try:
        result = sys.argv[1]
    except IndexError:
        print("lack of parameter example for xxx.py worker_status")
        exit(0)
    if result == "":
        print("lack of parameter example for xxx.py worker_status")
        exit(0)
    elif result == "worker_status":
         get_worker_status()