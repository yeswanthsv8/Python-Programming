print('Enter row & column of matrix1:')
p=int(input())
q=int(input())
matrix1=[[int(input()) for j in range(q)] for k in range(p) ]

print('Enter row & column of matrix2:')
x=int(input())
y=int(input())
matrix2=[[int(input()) for j in range(y)] for k in range(x)]

if q!=x:
    print('Matrix multiplication cannot be performed-')
    print("Column of Matrix1 != Row of Matrix2")
else:
    result=[[0 for j in range(y)] for k in range(p)]
    for i in range(p):
        for j in range(y):
            for k in range(x):
                result[i][j]=result[i][j]+matrix1[i][k]*matrix2[k][j]

    print('Resultant Matrix:')
    for i in range(p):
        for j in range(y):
            print(format(result[i][j],'<5'),end='')
        print()

