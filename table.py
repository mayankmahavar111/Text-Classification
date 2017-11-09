import os
from collections import defaultdict

table=defaultdict(list)
with open('unique.txt','rb') as f :
    x=f.read()
f.close()
x=x.split()
length=len(x)
print length
table['doc-title']=[]
for i in x:
    table[i]=[]

count=0
try:
    for j in os.listdir('stem/TRAIN/') :
        print count
        count=count+1
        with open('stem/TRAIN/'+j,'rb') as f:
            x=f.read().split()
        f.close()
        table['doc-title'].append(j)
        a = table['doc-title']

        for i in table:
            if i == 'doc-title':
                continue
            table[i].append(float(x.count(i))/float(len(x)))
except:
    pass

f=open('table.csv','wb')
temp=""
for x in table:
    temp+=str(x)+','
f.write(temp+'Class-Label,'+'\n')
for i in range(len(table['doc-title'])):
    print i , "section 2"
    temp=""
    for x in table:
        temp+=str(table[x][i])+','
    f.write(temp+'Class '+str(i)+','+'\n')
f.close()