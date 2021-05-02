s=int(input())
string=[input() for i in range(0,s)]

q=int(input())
query=[input() for i in range(0,q)]

vowels=['a','e','i','o','u']
count=0

for i in query:
    start=int(i[0])-1
    end=int(i[2])-1
    count=0
    for i in range(start,end+1):
        if string[i][0] in vowels and string[i][-1] in vowels:
            count+=1
    print(count)
            
            
    