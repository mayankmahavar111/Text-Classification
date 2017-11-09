from collections import defaultdict

test=defaultdict(list)

print len(test)

with open('unique.txt','rb') as f :
    x=f.read()
f.close()
x=x.split()
test['doc-title']=[]
for i in x:
    test[i]=[]


temp='0.txt'
with open('stem/TRAIN/'+temp,'rb') as f:
    x=f.read().split()
test['doc-title'].append(temp)
a=test['doc-title']

for i in test :
    if i=='doc-title':
        continue
    test[i].append(x.count(i))
temp='1.txt'
with open('stem/TRAIN/'+temp,'rb') as f:
    x=f.read().split()
test['doc-title'].append(temp)
a=test['doc-title']
print a.index(temp)
for i in test :
    if i=='doc-title':
        continue
    test[i].append(x.count(i))


print test['doc-title']
for x in test:
    if len(test[x]) !=2:
        print False
    if  test[x][1]!=0:
        print test[x]

"""
for i in range(10):
    test['key'].append(i)

print len(test['key'])
"""