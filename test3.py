import os

os.mkdir("Yes")
os.mkdir("No")

for i in range(0,22):
    os.mkdir("Yes/"+str(i)+'-b-sgm')
    os.mkdir("No/"+str(i)+'-b-sgm')