s1=input().lower()
res=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        if s1[i:j]==s1[i:j][::-1]:
            res.append(s1[i:j])
print(len(res))