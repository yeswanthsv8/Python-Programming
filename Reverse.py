s=input()
new=''    
i=len(s)-1

while(i>=0):
    new+=s[i]
    i-=1
s=new
print(s)
