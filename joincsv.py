f=open('table.csv','rb')
z=open('label.csv','rb')
t=open('tablereal.csv','wb')

table=f.readlines()
labels=z.readlines()
f.close()
z.close()
for i in range(len(table)):
    t.write(table[i].split('\n')[0]+','+labels[i].split(',')[1])
t.close()