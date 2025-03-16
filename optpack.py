from rectpack import newPacker,float2dec,PackingMode,PackingBin,SORT_NONE
from resource.app import predictedProfile,fixedCpuList,fixedMemList
from resource.pm import MEM,CPU
import random
from collections import defaultdict
containers=[]
for i in range(len(predictedProfile)):
    for j in range(predictedProfile[i]):
        containers.append((fixedCpuList[i],fixedMemList[i],i))

random.shuffle(containers)

packer=newPacker(mode=PackingMode.Offline,bin_algo=PackingBin.BBF,sort_algo=SORT_NONE,rotation=False)

dec_containers = [(float2dec(r[0], 3), float2dec(r[1], 3),r[2]) for r in containers]

for i in dec_containers:
    packer.add_rect(*i)

packer.add_bin(CPU,MEM,count=float("inf"))

packer.pack()

nPMs = len(packer)
# print(nPMs)

all_containers=packer.rect_list()

temp=defaultdict(list)

for r in all_containers:
    b,x,y,w,h,rid=r
    temp[b].append(rid)

containerMappedPM=[]
for i in temp:
    d=defaultdict(int)
    for a in temp[i]:
        d[a]+=1
    containerMappedPM.append(d)
    

