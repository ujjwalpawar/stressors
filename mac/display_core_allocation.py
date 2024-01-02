from operator import truediv
from posixpath import split
import json
import subprocess
from argparse import ArgumentParser


important_processes = {
    "l1app": "L1  ",
    "gnb_du_layer2": "DU  ",
    "duoam": "DU  ",
    "dumgr": "DU  ",
    "gnb_cu_pdcp": "CUUP", 
    "gnb_cu_l3": "CUCP", 
    "gnb_cu_rrm": "CUCP",
    "gnb_cu_son": "CUCP", 
    "gnb_cu_oam": "CUCP", 
    "bin_reader": "LOG "
}



def concise_print(d, ind=0):
    s = "".join([" "] * ind)
    cnt = 0
    for k,v in d.items():
        if cnt > 0:
            i = s
        else:
            i = ""
        i += "{}: ".format(k)
        print(i, end="")
        if type(v) is dict:
            if cnt > 0:
                i2 = 0
            else:
                i2 = ind
            concise_print(v, i2 + len(i))
        else:
            print(v, end="")
            print("\n", end="")
        cnt += 1


def dict_sort(d):
    d = dict(sorted(d.items()))
    for k,v in d.items():
        if type(v) is dict:
            d[k] = dict_sort(v)
    return d




aparser = ArgumentParser(prog='Display core allocation',
    epilog="Display core allocation for threads belonging to RAN.")
aparser.add_argument("-t", "--type", choices=["cpu", "nf"], 
                    default="nf",
                    help="cpu groups threads by CPU allocation and nf by function they belong to")

args = aparser.parse_args()



out = str(subprocess.check_output(["ps", "-e"])).split("\\n")

threads = []
for o in out:
    a = list(filter(None, o.split(" ")))
    if len(a) >= 3:
        found = False
        val = None
        for k,v in important_processes.items():
            if k in a[3]:
                val = v
                found = True
                break
        if val:
            out_thr = str(subprocess.check_output(["ps", "-T", "-o", "psr,tid,comm,cls,pri", "-p", a[0]])).split("\\n")
            cnt = 0
            for ot in out_thr:
                if cnt > 0:
                    at = list(filter(None, ot.split(" ")))
                    if len(at) >= 3  and at[3] != "<defunct>":
                        threads.append({
                            "tid": at[1],
                            "name": at[2], 
                            "cpu": format("{:2}".format(int(at[0]))),
                            "process_type": val,
                            "sched_policy": at[3],
                            "priority": at[4],
                        })
                cnt += 1


if args.type == "nf":
    disp = {}
    for t in threads:
        if not t["process_type"] in disp.keys():
            disp[t["process_type"]] = {}
        if not t["cpu"] in disp[t["process_type"]].keys():
            disp[t["process_type"]][t["cpu"]] = {}
        disp[t["process_type"]][t["cpu"]][t["name"] + "/" + t["tid"]] = "(" + t["sched_policy"] + "," + t["priority"] + ")"
    disp = dict_sort(disp)
    concise_print(disp)
else:
    disp = {}
    for t in threads:
        if not t["cpu"] in disp.keys():
            disp[t["cpu"]] = {}
        if not t["process_type"] in disp[t["cpu"]].keys():
            disp[t["cpu"]][t["process_type"]] = {}
        disp[t["cpu"]][t["process_type"]][t["name"] + "/" + t["tid"]] = "(" + t["sched_policy"] + "," + t["priority"] + ")"
    disp = dict_sort(disp)
    concise_print(disp)


