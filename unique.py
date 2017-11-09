import os


unique=[]
count=0
for x in os.listdir('stem/TRAIN/'):
    print count
    count=count+1
    with open('stem/TRAIN/'+str(x),'r') as f :
        temp=f.read()
    temp=temp.split()
    for x in temp:
        if x.isalpha() and (x not in unique) :
            unique.append(x)

f.close()

f=open('unique.txt','wb')
for x in unique:
    f.write(x+'\n')
f.close()
