#!/bin/bash
## Copyright (c) Microsoft Corporation. All rights reserved.

if [ ! -d "tcppump" ]; then
    echo "Creating tcppump."
    sudo tdnf install libpcap
    sudo tdnf install libpcap-devel
    git clone https://github.com/amartin755/tcppump.git
    pushd .
    cd tcppump
    rm -rf build/*
    cmake -B build
    cmake --build build
    popd
fi

labru1_ru_fh_mac="6c:ad:ad:00:08:86"
labru1_server_fh_mac="00:11:22:33:44:66"

labintru1_ru_fh_mac="6c:ad:ad:00:00:69"
labintru1_server_fh_mac="66:44:33:22:11:00"

devel5g3_server_fh_intf=eth1      # find this using sudo ip link

telco2_server_fh_intf=eth5      # find this using sudo ip link


# CHANGE THE FOLLOWING 3 LINES AS NEEDED
server_fh_intf=$telco2_server_fh_intf
server_fh_mac=$labru1_server_fh_mac
ru_fh_mac=$labru1_ru_fh_mac

delay=2
count=16
experiment="network-stress"

pushd .
cd ..

./exp_network_contention.sh $server_fh_intf $server_fh_mac $ru_fh_mac $delay $count $experiment

# Example usage :  ./exp_network_contention.sh <server-fh-intf> <server-fh-mac> <ru-fh-mac> <delay> <count> <experiment>
## delay : use 0 delay. 
## count : number of times to run the stress
## experiment : name of experiment 

popd

