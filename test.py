
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
    for x in lines[1:]:
        # print x.split(' ')[:1]
        if x.split(' ')[:1] == ['<REUTERS'] :
            count = count+1

    print count,j

    flag=0
    count = 0
    for x in lines[1:]:
        if flag == 0 :
            if x.split(' ')[:1] == ['<REUTERS'] :
                flag=1
                f = open(str(j)+'-b-sgm/' + str(count )+ '.txt', 'w')
                count = count +1
            continue
        if flag==1 and search("<BODY>",x)==True:
            f.write(x.split('<BODY>')[1])
            f.write('\n')
            flag = 2
            continue

        if flag ==2 :
            if "</BODY>" in x :
                flag =1
                continue
            f.write(x)
            f.write('\n')
        if flag==1 and '</REUTERS>' in x :
            flag=0

    f.close()