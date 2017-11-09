
def getLabel(x,dic):
    for i in dic:
        temp=i.split(' : ')
        #print temp[0],x,temp[0] =='TRAIN', temp[1] == x
        if  temp[0] =='TEST' and temp[1] == x :
            return temp[2].split('\n')[0]
    return "other"

def check(a,b):
    a=a.split(" ")[:-1]
    b=b.split(" ")[:-1]
    #print "This is a ", a,"and b" ,b
    for x in a :
        if x in b :
            return 1
    return 0


f=open('testing.csv','r')
testing=f.readlines()
f.close()
f=open('dic.txt','r')
dic=f.readlines()
f.close()

length=len(testing)-1
count = 0.0
for i in range(1,len(testing)-100):

    temp=testing[i].split(",")
    x=getLabel(temp[0],dic)
    if x == "other":
        count = count+1
        continue
    #print x ,",", temp[1].split('\n')[0],",",check(x,temp[1].split('\n')[0])
    if check(x,temp[1].split('\n')[0]) :
        count = count +1

print float(count)/float(len(testing) -100) , count , length
