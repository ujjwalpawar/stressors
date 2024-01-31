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

entity=CUUP
thread=pdcp_worker_0

core_id=$(python3 $HERE/get_core.py $entity $thread)
exit_code=$?

rm -f thread_list.txt

if [ $exit_code -ne 1 ]; then
    echo Core could not be found or thread $entity:$thread
    exit
fi

echo $entity:$thread is found on core $core_id

count=16

set -x
sudo python3 stressor.py -w $thread -p 0 -c $count -i $core_id  -d mixed_set2_anomaly -o 2200
set +x
## -w thread name
## -p priorty (increament priority of stressor by input value)
## -c count
## -i core id
## -d experiment name
## -o ops

popd

deactivate
