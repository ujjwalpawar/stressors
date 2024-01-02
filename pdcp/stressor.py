import subprocess
import argparse
global result
from datetime import datetime
import os


parser = argparse.ArgumentParser(description='Stressor for RAN based of stress-ng \n ******Warning: Do not set cpu-ops too high as it will cause system to crash******')
parser.add_argument('-w', '--worker', type=str, default="pdcp_worker_0", help='RAN worker name e.g pdcp_worker_0","f1_worker_0')
parser.add_argument('-p', '--priority', type=int, default=0, help='increament priority of stressor by input value (Default: 0 i.e equal to worker priority)')
parser.add_argument('-o', '--ops', type=int, default=1, help=' Number of operation executed by stressor (Default: 1) : Warning: Do not set this value too high as it will cause system to crash')
parser.add_argument('-c', '--count', type=int, default=1, help='Number of simultanious stressor (Default: 1)')
parser.add_argument('-i', '--id', type=int, default=1, help='Core ID to stress on ')
parser.add_argument('-d', '--dir', type=str, default="new", help='Experiment name')
args=parser.parse_args()
try:
    os.mkdir(args.dir,0o666)
except FileExistsError:
    print("Directory already exists")

print("stressing on :",args.worker)
print("priority of stressor is higher than workers priority by :",args.priority)
print(" Number of ops to run :",args.ops)
print(" Number of experiment :",args.count)

res=subprocess.check_output(str('sudo python3 display_core_allocation.py -t nf | grep '+ args.worker) , shell=True)
#byte to string conversion
res=res.decode("utf-8")

#extracting core id, scheduling policy anbd base priority of worker
#id=res.split(':')[0].split(" ")[-1]
id= int(args.id)
sch=res.split(':')[-1].split(",")[0].split("(")[-1]
base_priority=res.split(':')[-1].split(",")[1].split(")")[0]

print("{} running on core : {}".format(args.worker,id))
print("scheduling policy of worker : ",sch)
import pandas as pd

# Create an empty data frame

import time
current_time = datetime.now()
# Format the current time without spaces and with underscores
formatted_time = current_time.strftime('%Y-%m-%d_%H_%M_%S').replace(" ", "")
temp =[]
# Get the current time in nanoseconds
import random
# Display the current time in nanoseconds
sleep_start = 8
sleep_end = 10
per_mix = args.count / 4
for i in range(args.count):
    if(i // per_mix == 0):
        print("10% mix")
        args.ops = 800
        sleep_start = 8
        sleep_end = 10
    if(i // per_mix == 1):
        print("30% mix")
        args.ops = 2500
        sleep_start = 6
        sleep_end = 8
    if( i // per_mix == 2):
        print("50% mix")
        args.ops = 4500
        sleep_start = 4
        sleep_end = 6
    if( i // per_mix == 3):
        print("65% mix")
        args.ops = 6000
        sleep_start = 2
        sleep_end = 4
         
    current_time_ns = time.time_ns()    
    if(sch=='RR'):
        result=subprocess.run(['sudo', 'stress-ng', '--sched', 'rr', '--sched-prio', str(args.priority+int(base_priority)), '--taskset', str(id), '--cpu', str(1), '--cpu-ops', str(args.ops + random.randint(-500, 500))])
        #sudo stress-ng --sched < fifo/rr/etc> --sched-prio < scheduling priority> --taskset < core_id> --cpu 1 --cpu-ops < number of ops>
    if(sch=='FF'):
        #for fifo scheduling policy, priority is set to 40 less than base priority becuase of display_core_allocation.py script adds 40 to base priority
        result=subprocess.run(['sudo', 'stress-ng', '--sched', 'fifo', '--sched-prio', str(args.priority+int(base_priority)-40), '--taskset', str(id), '--cpu', str(1), '--cpu-ops', str(args.ops + random.randint(-500, 500))])
    if(sch=='TS'):
            result=subprocess.run(['sudo', 'stress-ng', '--sched', 'other', '--sched-prio', str(args.priority+int(base_priority)), '--taskset', str(id), '--cpu', str(args.count), '--cpu-ops', str(args.ops + random.randint(-500, 500))])
    end_time_ns = time.time_ns()
    temp.append([current_time_ns, end_time_ns])
    sleep_time = random.uniform(sleep_start, sleep_end)
    print("sleep for :{}".format(sleep_time))
    df = pd.DataFrame(temp, columns=['start_time', 'end_time'])
    filename = "./"+args.dir+"/"+args.worker+"_"+str(formatted_time)+".csv"
    df.to_csv(filename)
    # Sleep for the generated time
    time.sleep(sleep_time)
    
print(result.returncode)
import os
new_permissions = 0o777
os.chmod(filename, new_permissions)

