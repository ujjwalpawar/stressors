# Prerequisites

## Depends on stress-ng. 

Install stress-ng (apt, yum).

# To run
```
cd execution
./run_it.sh
```
## To alter the behaviour of the test, edit run_it.sh and change the parameters of stressor.py....

```
stressor.py -w pdcp_worker_0 -p 0 -c 16 -i 10 -d mixed_set2_anomaly -o 2200
```
where 
```
-w thread name
-p priorty (increament priority of stressor by input value)
-c count
-i core id
-d experiment name
-o ops
```
