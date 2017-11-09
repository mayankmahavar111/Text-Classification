import os


with open('unique.txt','rb') as f :
    x=f.read()
f.close()
x=x.split()
temp="doc-title,"
for i in range(len(x)):
    if i==len(x)-1:
        temp+=x[i]
        break
    temp+=x[i]+','

t=open('table.csv','wb')
t.write(temp+'\n')
for x in os.listdir('table/'):
    with open('table/'+x ,'rb') as f:
        t.write(f.read()+'\n')

f.close()
t.close()