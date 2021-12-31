
    python3 trouble_shooting.py <parameter>

all_worker_status 统计当前worker机，p1,p2,c2运行时间情况，统计日算力

worker_status <host_ip> 统计指定worker,p1,p2,c2运行时间情况，统计日算力

fix_worker_check 获取当前运行异常的worker(显卡，硬盘，日志信息)

check_worker  <host_ip> 获取按规定worker(显卡，硬盘，日志信息)运行情况

fix_worker_restart 重启当前运行异常worker服务
 
worker_stop <host_ip> 停止指定worker服务

worker_start <host_ip> 指定指定worker服务

miner_disk_status 获取miner nfs挂盘是否异常

miner_gpu_status  获取miner gpu信息是否异常

storage_to_miner_network   获取storage到miner网口速率

miner_to_storage_network   获取miner到storage网口速率

winning_block <day> 指定多少天内统计出块权数量

lost_block_check <time> 指定时间进一步获取丢失块日志

lost_sectors 掉算力，初步排查（常见问题日志）

restart_host <host_ip> 重启指定机器

quickly_check 掉算力后miner快速排查（gpu,nfs磁盘挂载,M<->S网络状态，报错日志）
