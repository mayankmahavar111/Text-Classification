import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer ,WordNetLemmatizer

output =[]
stop=set(stopwords.words('english'))
stemmer = PorterStemmer()
lemma =WordNetLemmatizer()
for j in range(22):
    if j >9 :
        with open('reut2-0'+str(j)+'.sgm','r') as f:
            text=f.readlines()
    else:
        with open('reut2-00'+str(j)+'.sgm','r') as f:
            text=f.readlines()
    for x in text:
        if 'LEWISSPLIT' in x:
            test=x.split('LEWISSPLIT="')[1]
            test=test.split('"')[0]
            output.append(test)
    f.close()
output=list(set(output))
print output

try:
    os.makedirs('stem')

    for x in output:
        os.makedirs('stem/'+str(x))
except:
    pass

count=0
for j in range(len(output)):
    lis=os.listdir('lewisplit/'+str(output[j]))
    for i in lis:
        print count
        count=count+1
        f=open('lewisplit/'+str(output[j])+'/'+i)
        text=f.read()
        token=word_tokenize(text)
        filtered=[]
        try:
            for x in token:
                if x.lower() not in stop and x.isdigit() == False and x!=',':
                    filtered.append(str(stemmer.stem(x)))
            test=""
            for x in filtered:
                if x == '.':
                    test+='.'+'\n'
                else:
                    test+=x+' '
            t=open('stem/'+str(output[j])+'/'+i,'wb')
            t.write(test)
            t.close()
        except:
            continue
