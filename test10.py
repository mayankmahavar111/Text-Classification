import os
import time


def getLabel(x,dic):
    for i in dic:
        temp=i.split(' : ')
        #print temp[0],x,temp[0] =='TRAIN', temp[1] == x
        if  temp[0] =='TRAIN' and temp[1] == x :
            return temp[2].split('\n')[0]
    return "other"

def findvalue(x,dic,val):
    label=getLabel(x,dic)
    #print label

    for i in val:
        temp=i.split(" ")
        #print temp[0],label, temp[0]+" "==label
        if temp[0]+" "==label :
            return float(temp[1].split('\n')[0])
    return 0

f=open('dic.txt','r')
dic=f.readlines()
f.close()
f=open('docprob.txt','r')
val=f.readlines()
f.close()
f=open('testtable/0.txt','r')
x=f.read()
f.close()
x=x.split(',')
dir=os.listdir('stem/TRAIN')
max=0
index=0
t=time.time()
for i in range(len(x)):
    print i
    temp=findvalue(dir[i],dic,val)
    if max< float(x[i])*temp:
        max=float(x[i])*temp
        index=i
print max,index, dir[index],getLabel(dir[index],dic)

print "time is ",time.time()-t