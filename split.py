import os
import re

output =[]
for j in range(22):
    if j >9 :
        with open('reut2-0'+str(j)+'.sgm','r') as f:
            text=f.readlines()
    else:
        with open('reut2-00'+str(j)+'.sgm','r') as f:
            text=f.readlines()
    for x in text:
        if 'LEWISSPLIT' in x:
            test=x.split('LEWISSPLIT="')[1]
            test=test.split('"')[0]
            output.append(test)
    f.close()
output=list(set(output))
print output

try:
    os.makedirs('lewisplit')

    for x in output:
        os.makedirs('lewisplit/'+str(x))
except:
    pass

dic={}
for x in output:
    dic[x]=0

count=0
z=open('dic.txt','wb')
abc="other"
for j in range(22):
    if j > 9 :
        f = open('reut2-0'+str(j)+'.sgm', 'r')
    else:
        f= open('reut2-00'+str(j)+'.sgm', 'r')

    lines=f.read()
    lines=re.split('<BODY>|</BODY>',lines)
    for i in range(len(lines)):
        print count
        count=count+1
        if i%2==1:
            continue
        if i==len(lines)-1:
            break
        ab = re.split('<TOPICS>|</TOPICS>', lines[i])[1]
        ab = re.split('<D>|</D>', ab)[1::2]
        if len(ab) == 0:
            abc = "other"
        else:
            abc = ""
            for x in ab:
                abc += str(x) + " "
        test = lines[i].split('LEWISSPLIT="')[1]
        test = test.split('"')[0]
        t=open('lewisplit/'+test+'/'+str(dic[test])+'.txt','wb')
        z.write(test+" : "+str(dic[test])+'.txt : '+abc +'\n' )
        t.write(lines[i+1])
        dic[test]+=1
        t.close()
f.close()
z.close()