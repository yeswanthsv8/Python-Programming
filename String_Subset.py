n1=input().lower()
n2=input().lower()
l=[]

for i in n1:
    if i in n2:
        l.append(n2.count(i))
        n2=n2.replace(i,'',1)

print(min(l))