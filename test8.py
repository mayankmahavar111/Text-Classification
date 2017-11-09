from collections import defaultdict


table=defaultdict(list)
f=open('table.csv','r')
lis=f.readlines()
f.close()
temp=lis[0].split(',')

x=len(lis[0].split(','))
for i in range(1,3):
    temp2 = lis[i].split(',')
    for j in range(x):
        table[temp[j]].append(temp2[j])
print table[temp[0]][0],len(table[temp[0]])
table[temp[0]][0]=12
print table[temp[0]][0],len(table[temp[0]])