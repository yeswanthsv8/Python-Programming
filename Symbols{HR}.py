s=input()

#l=['+','-','*','/','=']

l=[s.count('+'),s.count('-'),s.count('*'),s.count('/'),s.count('=')]
print(min(l))