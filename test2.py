import os
import re



with open('reut2-000.sgm','rb') as f :
    test=f.read()
lines=re.split('<BODY>|</BODY>',test)
test=re.split('<TOPICS>|</TOPICS>',test)

print len(lines),len(test)
print lines[1]
print len(re.split('<D>|</D>',test[5])[1::2])