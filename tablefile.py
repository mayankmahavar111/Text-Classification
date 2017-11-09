import os
from collections import defaultdict

table=defaultdict(list)
with open('unique.txt','rb') as f :
    x=f.read()
f.close()
table=x.split()

count=0
try :
    os.makedirs('table')
except Exception as e:
    print e
    pass



for j in os.listdir('stem/TRAIN/') :
    if j.endswith('.txt') == False :
        continue
    print count
    count=count+1
    with open('stem/TRAIN/'+j,'rb') as f:
        x=f.read().split()
    f.close()
    f=open('table/'+str(j),'wb')
    temp=j+','
    for i in range(len(table)):
        if i==len(table)-1:
            temp += str(float(x.count(table[i])) / float(len(x)))
            break
        temp+=str(float(x.count(table[i]))/float(len(x)))+','
    f.write(temp)

