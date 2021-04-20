s1=input().lower()
s2=input().lower()

l2=len(s2)
count=j=0

for i in range(0,len(s1)):
    if j<l2:
        if s1[i]==s2[j]:
            count+=1
        j+=1
    else:
        break
print(count)