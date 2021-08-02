s=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
l=[]

for i in s:
    if i in vowels:
        l.append(s[0:s.index(i)+1])
        s=s.replace(s[0:s.index(i)+1],'')

if len(s)>0:
    l.append(s)

for i in range(0,len(l)):
    if i%2!=0:
        if i==len(l)-1:
            if l[i][-1] in vowels:
                l[i]=l[i][::-1]
            else:
                pass
        else:
            l[i]=l[i][::-1]
        
    print(l[i],end='')