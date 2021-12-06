n=input()
upp=''
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        upp+=i

upp=upp.lower()
n=n.lower()
ss=''
ss+=min(n)    
n=n.replace(min(n),'',1)
n=list(sorted(n))


for i in n:
    if i>ss[-1]:
        ss+=i
        ind=n.index(i)
        n[ind]='#'
 
n=''.join(n)
n=n.replace('#','')


n=n[::-1]
for i in n:
    if i<=ss[-1]:
        ss+=i
        n=n.replace(i,'#',1)
    
for i in ss:
    if i in upp:
        ss=ss.replace(i,i.upper(),1)
        break
        
print(ss)
    