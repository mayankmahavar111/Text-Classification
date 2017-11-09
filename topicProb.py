import os
import re

dic={}

for j in range(22):
    print j
    if j >9 :
        with open('reut2-0'+str(j)+'.sgm','r') as f:
            x=f.read()
    else:
        with open('reut2-00'+str(j)+'.sgm','r') as f:
            x=f.read()
    f.close()
    test=re.split('<BODY>|</BODY>',x)

    #print 'TOPICS="YES"' in test[0]

    for i in range(len(test)):
        if i%2==1:
            continue
        if 'TOPICS="YES"' in test[i]:
            temp=re.split('<TOPICS>|</TOPICS>',test[i])[1]
            temp=re.split('<D>|</D>',temp)[1::2]
            for x in temp:
                try:
                    dic[x]+=1
                except:
                    dic[x]=1

count=0
for x in dic:
    count+=dic[x]
print count

f=open('docprob.txt','wb')
for x in dic:
    f.write(str(x)+" "+str(float(dic[x])/float(count))+'\n')
f.close()


print len(test)
