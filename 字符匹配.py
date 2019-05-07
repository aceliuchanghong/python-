import os
import re
s=''
f1=open('0.txt','r+')
#f2=open('1.txt','w+')
a=f1.readline()
s=s+a
b=re.findall(r"com(.+?)png",s)
#print(b)
for c in b :
    print('http://file-1.book118.com'+c+'png')
#print(s)
f1.close()
#f1.close()
https://www.jb51.net/article/99453.htm
