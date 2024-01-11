#!/bin/bash
## Copyright (c) Microsoft Corporation. All rights reserved.

if [ ! -d ".venv" ]; then
    echo "Creating virtualenv."
    ./init_venv.sh
fi

source .venv/bin/activate

HERE=$(pwd)

pushd .
cd ..

rm -f thread_list.txt
sudo python3 display_core_allocation.py -t nf > thread_list.txt

entity=DU
thread=SlotHlr_DU1_C0

core_id=$(python3 $HERE/get_core.py $entity $thread)
exit_code=$?

rm -f thread_list.txt

if [ $exit_code -ne 1 ]; then
    echo Core could not be found or thread $entity:$thread
    exit
fi

echo $entity:$thread is found on core $core_id

make

ops=185000
count=24
exp=mac_stress

set -x
sudo taskset -c $core_id chrt -f 99 ./mac_stressor $ops $count $exp
set +x
## -ops : number of time while loop will run. Use 165000 works
## -count : number of time to run stress
## -exp : name of experiment

popd

deactivate
