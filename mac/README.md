# Compile using gcc
use sudo python3 display_core_allocation.py -t nf
# to get core on which slothlr_du1_c0 is running. 
# Usage : 
sudo taskset -c \<core on which SlotHlr_DU1_C0\> chrt -f 99 ./mac_stressor \<ops\> \<count\> \<exp name\>
## -ops : number of time while loop will run. Use 165000 works 
## -count : number of time to run stress
## -exp : name of experiment 

