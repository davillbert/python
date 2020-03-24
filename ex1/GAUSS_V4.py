A = [
    [1, 2, 3, 5],#, 8],  # 0 0 = 1     0 1 = 2     0 2 = 3
    [4, 5, 6, 10],#, 9], 
    [7,8,9, 12]#,17]#,  ## 1 0 = 4     1 1 = 5    1 1 = 6
   # [7, 8, 9, ]  # 2 0 = 7    2 1 = 8   2 2 = 9
]

b = [1, 1,1]#, 1]


# 1 - умножение на чиселку
# 2 - перестановка
# 3 - сложение
# 1) и 3)
# 4 - вывод на экран

def umnozhit(Matrix, Free, str, number, n):
   # for j in range(n):
    #    Matrix[str][j] = Matrix[str][j] * number
    Free[str] = Free[str] * number
    Matrix[str] = [Matrix[str][j] * number for j in range(n)]

def perestanovka(Matrix, Free, str1, str2):
    s = Matrix[str1]
    Matrix[str1] = Matrix[str2]
    Matrix[str2] = s
    t = Free[str1]
    Free[str1] = Free[str2]
    Free[str2] = t


def slozhenie(Matrix, Free, str1, str2, n):
    for j in range(n):
        Matrix[str1][j] = Matrix[str1][j] + Matrix[str2][j]
    Free[str1] = Free[str1] + Free[str2]


def sloz_umnoz(Matrix, Free, str1, str2, number, n):
    for j in range(n):
        Matrix[str1][j] = Matrix[str1][j] + number * Matrix[str2][j]
    Free[str1] = Free[str1] + number * Free[str2]


def printM(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()


def printF(Free):
    for i in range(len(Free)):
        print(Free[i], end=' ')
        print()


def Gauss(Matrix, Free):
    str = 0
    while (str < len(Free)):
        stl_max = -1
        for r in range( len(Matrix[str]) ):
            if (Matrix[str][r] != 0):
                stl_max = r
                break
                #print(r)
               # print(Matrix[str][r] != 0)
        if (stl_max == -1):
            print("No solutions")
        # return 0
        
        umnozhit(Matrix, Free, str, 1 / Matrix[str][stl_max], len(Matrix[str]))
      #  print("================A================")
       # printM(A)

        for r in range(len(Free)):
            if(r!=str):
                sloz_umnoz(Matrix, Free, r, str, -1 * Matrix[r][stl_max], len(Matrix[str]))

        #if ((stl_max != str) and (stl_max <= len(Matrix))):
         #  perestanovka(Matrix, Free, stl_max, str)
    #    else:
       # print("================A================")
      #  printM(A)
        str = str + 1
        #stl_max = -1

#printM(A)


Gauss(A, b)

k=0
x = 0
for r in range(len(A)):
    for l in range(len(A[r])):
       if A[r][l]==0:
           k=k+1
    if k == len(A[r]):
        x = x + 1
        k = 0
    
rg = len(A) - x 





print("================rg================")
print(rg)

print("================A================")
printM(A)
print("================b================")
printF(b)

N = len(A)
M = len(A[0]) - rg
F = [[0] * M for i in range(N)]


            

for i in range(N):
    for j in range (M):
        F[i][j] = - A[i][j + len(A[0]) - rg] 

print("================F================")
printM(F) 
