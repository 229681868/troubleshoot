#!/usr/bin/python
import os
import re
import datetime

class Miner:

    def miner_disk_status(self):
        cmd ='cat ~/share/ssd/data/lotus`sudo supervisorctl status \
             |cut -d" " -f1 \
             |grep miner`/storage.json \
             |grep -iw path|cut -d ":" -f 2'

        disk_list =  os.popen(cmd).read().strip('"').strip().split("\n")
        disk_not_found_result=""
        for var in disk_list:
            cmd="timeout 0.5 cat {0}/sectorstore.json".format(var)
            check_result=os.popen(cmd).read()
            if  check_result.find("Weight") < 0:
                 disk_not_found_result+="\033[1;31;40m {0} disk not found \033[0m".format(var)+"\n"
        return disk_not_found_result


    def miner_gpu_status(self):
        cmd = 'cat /home/ps/share/hdd/log/miner*.log| \
               grep -i gpu| \
               tail -n 18'
        gpu_info = os.popen('nvidia-smi').read()
        gpu_log = os.popen(cmd).read()
        if gpu_log.lower().find("error")>0:
            print("\033[1;31;40m gpu error {0} \033[0m".format(gpu_log[gpu_log.lower().find("error"):]))
        gpu_info+="\n"+gpu_log
        return gpu_info

    def minerTostorage_network(self):
        os.system('iperf -s >> /tmp/network_minerToStorage.log&')
        os.system('fab iperf')
        os.system('cat /tmp/network_minerToStorage.log')
        os.system('pkill iperf&&cp /dev/null /tmp/network_minerToStorage.log')


    def winning_block(self,day):
       time_range = ""
       for i in range(0,int(day)):
            time_range = time_range+"|"+str(datetime.date.today() - datetime.timedelta(i))
       time_range=time_range.replace("|","",1)

       cmd='cat ~/share/hdd/log/$(sudo supervisorctl status|cut -d" " -f1|grep miner).log* \
           |egrep -i \"{0}\"| \
           egrep -i "generatewinningpost"'.format(time_range)

       block_info=os.popen(cmd).read()
       block_info=block_info.replace('"logger":"storageminer","caller":"storage/miner.go:297",',"").replace('"level":"info","ts":',"").replace('"msg":',"")
       print(block_info)
       block_info=block_info.strip().split("\n")
       block_num_from_log=len(block_info)
       return block_num_from_log


    def lost_sectors_info(self):
        cmd='cat /home/ps/share/hdd/log/$(sudo supervisorctl status|cut -d" " -f1|grep miner).log \
            |egrep -i "sector file stat error \
            |running window post failed \
            |time out"'
        lost_sectors_info = os.popen(cmd).read().strip()
        return lost_sectors_info



