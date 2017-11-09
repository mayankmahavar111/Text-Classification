import os
import time
try:
    os.makedirs('testtable')
except:
    pass
flag=1
t=time.time()
for k in os.listdir('stem/TEST/'):
    print flag
    flag+=1
    with open('stem/TEST/'+k,'r') as f:
        test=f.read()
    f.close()
    unique=[]
    test=test.split()
    for x in test:
        if x not in unique  and  x.isalpha():
            unique.append(x)
    ab=os.listdir('stem/TRAIN/')
    string=""

    for j in range(len(ab)):
        #print j
        with open('stem/TRAIN/'+ab[j],'rb') as f:
            x=f.read().split()
        count=0
        for i in unique :
            count+=float(x.count(i))/float(len(x))
        if j==len(ab)-1:
            string+=str(count)
            break
        string+=str(count)+','
    #break
    f=open('testtable/'+k,'wb')
    f.write(string)
    f.close()
print time.time()-t