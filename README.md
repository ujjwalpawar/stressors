Stressor for different type of anomaly.  

## Commands used to generate the traffic 
**iperf3 dl tcp** `iperf3 -c 11.11.11.11 -l 1320 -t 600` 
**iperf3 ul tcp ** `iperf3 -c 11.11.11.11 -l 1320 -t 600 -R` 
**iperf3 dl udp** `iperf3 -c 11.11.11.11 -l 1320 -t 200 -u -b 10M` 
**iperf3 ul udp** `iperf3 -c 11.11.11.11 -l 1320 -t 200 -u -b 10M -R`  
** file dl ** `wget https://speed.hetzner.de/1GB.bin`  
**file ul** Use scp to copy a dummy file to generate file ul traffic.
**video** `mpv https://www.dailymotion.com/video/x7xtdoc -vo=null -v` (requires mpv to be installed `sudo apt install mpv`)

## Example mac stressor with iperf3 tcp dl traffic

1. Generate iperf3 traffic tcp dl traffic using above mentioned command.
2. Go to mac folder and run mac_stressor using following command `sudo taskset -c <core on which SlotHlr_DU1_C0> chrt -f 99 ./mac_stressor 185000 24 mac_stress`
3.  This will result in 5-10% drop in throughput. Try changing 185000 value to get more or less stress.
    
## Example pdcp stressor with iperf3 tcp dl traffic

1. Generate iperf3 traffic tcp dl traffic using above mentioned command.
2. Go to pdcp folder and run mac_stressor using following command `sudo python3 stressor.py -w pdcp_worker_0 -p 0 -c 16 -i <core on which pdcp_worker_0 is running> -d exp-1 -o 2200`
3. This will result in 5-10% drop in throughput. Try changing 185000 value to get more or less stress.
    
