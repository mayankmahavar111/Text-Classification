import re
"""
f=open('reut2-000.sgm','r')

lines=f.read()
lines=re.split('<BODY>|</BODY>',lines)
#print len(lines)
#print lines[0]
test=lines[0].split('LEWISSPLIT="')[1]
test=test.split('"')[0]
print test
"""
a={}
b=['a','c','d']
a[b[0]]=0
for i in range(3):
    a[b[0]]+=1
print a