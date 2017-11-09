import os
import math

dic={}
lis=os.listdir('stem/')
count=0
length=0
for j in lis:
    for k in os.listdir('stem/'+j+'/'):
        print count
        count=count+1
        f=open('stem/'+j+'/'+k)
        length=length+1
        lines=f.read()
        lines=lines.split()
        for x in lines:
            dic[x]=(float(lines.count(x))/float(len(lines)))

f.close()

count=0
id={}
for j in lis:
    for k in os.listdir('stem/' + j + '/'):
        print count
        count = count + 1
        f = open('stem/' + j + '/' + k)
        lines = f.read()
        for i in dic:
            if i in lines:
                try:
                    id[i]+=float(1)
                except:
                    id[i]=float(1)

f=open('tf.txt','wb')
for i in dic:
    f.write(str(i)+' '+str(dic[i]*math.log(float(length)/id[i]))+'\n')
f.close()