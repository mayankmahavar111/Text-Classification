import os

def check(x):
    x = x.replace("\n","")
    if not os.path.exists("Topics/"+x):
        os.makedirs("Topics/"+x)
    return x

def spli(x):
    x=x.split('<TOPICS>')[1]
    x=x.split('</TOPICS>')[0]
    x=x.split('<D>')
    x=x.split('</D>')
    return x

def findD(x):
    x=x.split('<TOPICS>')[1]
    x=x.split('</TOPICS>')[0]
    x = x.split('<D>')
    return len(x)

def search(x,line):
    return x in line

for j in range(22):
    if j >9 :
        with open('reut2-0'+str(j)+'.sgm','r') as f:
            lines=f.read().splitlines()
    else:
        with open('reut2-00'+str(j)+'.sgm','r') as f:
            lines=f.read().splitlines()
    count = 0
    line = ""
    for x in lines:
        # print x.split(' ')[:1]
       # if x.split(' ')[:1] == ['<REUTERS'] :
            #count = count+1
        line = line + "\n" + x

    print count,j

    topic = 0
    flag=0
    count = 0
    k=0
    temp= line.split('<REUTERS')
    line = ""
    for  x in temp:
        line =  line + "\n" + x
    line=line.split('</REUTERS>')
    for  x in line :
        try:
            x = x.split('<TOPICS>')[1]
            t= x.split('</TOPICS>')[0]
        except :
            break
        temp=t.split('<D>')
        t= ""
        for test in temp:
            t = t +"\n" + test
        t=t.split('</D>')
        if len(t) == 0:
            print  count
            f = open("Topics/no topic"+str(j)+'-' + str(count )+ '.txt', 'w+')
            f.write(x.split('</TOPICS>')[1])
            f.write('\n')
            count = count +1
            continue
        for d in t:

            d=check(d)
            print count
            f = open("Topics/"+d+"/"+str(j)+'-topic-' + str(count )+ '.txt', 'w+')
            test = x.split('</TOPICS>')[1]
            try :
                test= test.split('<BODY>')[1]
                test = test.split('</BODY>')[0]
            except:
                break
            f.write(test)
            f.write('\n')
        count = count + 1

    f.close()
