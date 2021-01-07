s=input()
c=0
l=list(map(int,s[1:len(s)-1].split(',')))
l.sort()
s=set()

for i in l:
    for j in l:
        if i<j and (i+j)%2!=0:
            s.add((i,j))
print(len(s))
