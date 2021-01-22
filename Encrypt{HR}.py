s=input()
l=len(s)
out=''

if l%2==0:
    for i in s[::-1]:
        x=ord(i)+l
        if i.islower and x>122 or i.isupper() and x>90:
            x=x-26
        out+=chr(x)
        l-=1
    out=out[::-1]
    
       
else:
     for i in s:
        x=ord(i)+l
        if i.islower and x>122 or i.isupper() and x>90:
            x=x-26
        out+=chr(x)
        l-=1
print(out)
    