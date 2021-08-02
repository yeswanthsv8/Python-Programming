import re
s=input().lower()
s=re.sub('[^a-z]',"",s)

l=sorted(s)
new=''.join(l)
count=0

for i in new:
    if new.count(i)>1:
        print(i,'-',new.count(i))
        new=new.replace(i,'',new.count(i))
        count+=1
        
if count==0:
    print('No duplicate characters')