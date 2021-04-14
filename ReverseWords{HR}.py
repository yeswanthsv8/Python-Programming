def change(str,case):
    l=str.split(' ')
    new=''
    
    if case==0:
        for i in range(0,len(l)):
            new=new+l[i][::-1]
            if i!=len(l)-1:
                new=new+' '
        print(new)
        
    elif case==1:
        ind=[]
        for i in range(0,len(str)):
            if str[i].isupper():
                ind.append(i)

        
        for i in range(0,len(l)):
            new=new+l[i][::-1]
            if i!=len(l)-1:
                new=new+' '
            new=new.lower()
        
        temp = list(new)
        for i in range(0,len(new)):
            if i in ind:
                temp[i] = new[i].upper()
                string = "".join(temp)
        print(string)
        
        
                
    else:
        return '-1'
    
        
str=input()
case=int(input())
change(str,case)
