n=input()
l=[]
s=""

if len(n)%2==0:
    j=0
    for i in range(1,len(n)+1):
        val=ord(n[j])+i
        if ( val>90 and ord(n[j])>=65 and ord(n[j])<=90 ) or ( val>122 and ord(n[j])>=97 and ord(n[j])<=122 ):
            val=val-26
        
        s=s+chr(val)
        j+=1

else:
    j=0
    for i in range(len(n),0,-1):
        val=ord(n[j])+i
        if ( val>90 and ord(n[j])>=65 and ord(n[j])<=90 ) or ( val>122 and ord(n[j])>=97 and ord(n[j])<=122 ):
            val=val-26
        
        s=s+chr(val)
        j+=1

print(s)