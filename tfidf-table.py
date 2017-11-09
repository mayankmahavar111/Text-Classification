from collections import defaultdict

k=5000
ab=0
table=defaultdict(list)
f=open('table.csv','r')
lis=f.readlines()
f.close()
temp=lis[0].split(',')
x=len(lis[0].split(','))
for i in range(0,9):
    if i==8:
        k=17264
    else:
        k=(i+1)*2000
    ab=(i)*2000
    try:
        for abc in temp:
            table[abc]=[]
        print "Hello World"
        lisLength = len(lis)
        for i in range(1,lisLength):
            if i>k:
                break
            if i<ab:
                continue
            temp2=lis[i].split(',')
            for j in range(x):
                table[temp[j]].append(temp2[j])
        print "checkpoint"
        print (float(table[temp[0]][0]))
        length=x

        for i in range(1,lisLength):
            print i,"section 2"
            if i>k:
                break
            if i<ab:
                continue
            for x in temp:
                if x=='doc-title' or x=='Class-Label' or x=='':
                    continue
                #print table[x][i]
                try:
                    table[x][abs(i-ab)]=round(float(table[x][abs(i-ab)])/float(length),5)
                except:
                    continue


        print "Hello World Again"
        t = open('tfidf-'+str(ab/2000)+'.csv', 'wb')
        if ab == 0:
            test=''

            for i in range(length):
                if i==length-1:
                    test+=temp[i]
                    break
                test+=temp[i]+','
            t.write(test)
        for i in range(1,lisLength):
            print i,k,ab,i>k-2,i<ab+2,abs(i-ab)
            if i>k-1:
                break
            if i<ab+1:
                continue
            test=''
            for x in range(length):
                if x==length-1:
                    test+=str(table[temp[x]][abs(i-ab)])
                    break
                test+=str(table[temp[x]][abs(i-ab)])+','
            t.write(test)

        print "choose to see the positive."

    except Exception as e:
        print e

t.close()