import time

f= open('stem/TEST/2.txt','rb')
x=f.read()
f.close()
test=x.split()
unique=[]
t=time.time()
for x in test:
    if x.isalpha() and (x not in unique):
        unique.append(x)
t-=time.time()
print "First :",t
t=time.time()
print "Got unique"
f=open('tablereal.csv','rb')
ab=f.readlines()
f.close()
f=open('docprob.txt','rb')
temp2=f.readlines()
f.close()
y=ab[0]
test=y.split(',')
max=0
print len(ab)
t-=time.time()

for i in range(1,len(ab)):
    print i
    x=ab[i]
    #print x.split(',')[0],x.split(',')[-1]

    temp=x.split(',')
    #print temp[-1].split('\n')[0] == "other",temp[-1].split('\n')[0]
    t=time.time()
    if temp[-1].split('\n')[0] == "other":
        continue
    count=0
    for i in range(1,len(test)-1):
        if test[i] in unique:
            count+=float(temp[i])
    t-=time.time()
    t=time.time()
    #print count
    #print temp[-1].split('\n')[0] == 'cocoa',temp[-1] ,len(temp[-1])
    for j in temp2:
        #print temp[-1] == i.split(" ")[0],temp[-1],i.split(" ")[0]
        if temp[-1].split('\n')[0] == (j.split(" ")[0]+" " ):
            break
    if max <count:
        max=count
        label=temp[-1]
print max,label
