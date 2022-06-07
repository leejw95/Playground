import enum
import sys
import os

f = open('D_FF_test\D_Latch.pex.netlist','r')
lines = f.readlines()
subckt_list = []
i = 0
for index,line in enumerate(lines) : 
    if '.subckt' in line :
        subckt_list.append(line)
        i = index
    if (index == i + 1) and '+' in line :
        subckt_list.append(line)
        i = i + 1

l = subckt_list[0].split()
l.pop(0)
ckt_name = l[0]
# print (ckt_name)
l[0] = 'x'+ l[0]
# print (l)
print (ckt_name)
l = " ".join(l)
print (l)
subckt_list[0] = l
print (subckt_list)

ll = subckt_list[-1].split()
# print (ll)
ll.append(ckt_name)
print (ll)
ll = " ".join(ll)
subckt_list [-1] = ll
print (subckt_list)

lines = lines + subckt_list
# print (lines)
new_lines = "".join(lines)

print (new_lines)

f.close() 

with open('D_FF_test\\new.pex.netlist','w') as f :
    f.write(new_lines)
    f.close()
