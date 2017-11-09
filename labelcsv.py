import os


def findlabel(key):

    for i in test:
        if i.split(" : ")[1] == key:
            return i.split(" : ")[2]

f=open('dic.txt','rb')
x=f.readlines()
f.close()
#print "TRAIN " in x[0].split(":")
test=[]
for i in x:
    if "TRAIN " in i.split(":"):
        test.append(i)

f=open('label.csv','wb')

f.write('doc-title,ClassLabel'+'\n')

for j in os.listdir('table/'):
    f.write(str(j)+','+findlabel(j))
f.close()