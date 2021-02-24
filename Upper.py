s=input()
s1=''

for i in range(0,len(s)):
    if ord(s[i])>=97 and ord(s[i])<=122:
        s1+=chr(ord(s[i])-32)
    else:
        s1+=s[i]
print(s1)
