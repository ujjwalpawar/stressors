
# To run
```
cd execution
./run_it.sh
```
## To alter the behaviour of the test, edit run_it.sh and change the parameters of "taskset" command....
```
sudo taskset -c \<core on which SlotHlr_DU1_C0\> chrt -f 99 ./mac_stressor \<ops\> \<count\> \<exp name\>
```
where 
```
-ops : number of time while loop will run. Use 165000 works 
-count : number of time to run stress
-exp : name of experiment 
```

