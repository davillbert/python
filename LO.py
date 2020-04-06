
def umnozhit(Matrix, Free, str, number, n):
    for j in range(n):
        if (Matrix[str][j] == int(Matrix[str][j])):
            Matrix[str][j] = Matrix[str][j] * number
        else:
            Matrix[str][j] = round(Matrix[str][j] * number, 15)
    if (Free[str] == int(Free[str])):
        Free[str] = Free[str] * number
    else:
        Free[str] = round(Free[str] * number, 15)


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
        if (Matrix[str1][j] == int(Matrix[str1][j])):
            Matrix[str1][j] = Matrix[str1][j] + number * Matrix[str2][j]
        else:
            Matrix[str1][j] = round(Matrix[str1][j] + number * Matrix[str2][j], 15)
    if (Free[str1] == int(Free[str1])):
        Free[str1] = Free[str1] + number * Free[str2]
    else:
        Free[str1] = round(Free[str1] + number * Free[str2], 15)


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
        stl_max = None
        for r in range(len(Matrix[str])):
            if (Matrix[str][r] != 0):
                stl_max = r
                break

        if (stl_max == None):
            print(" ")
            break

        umnozhit(Matrix, Free, str, 1 / Matrix[str][stl_max], len(Matrix[str]))

        for r in range(len(Free)):
            if (r != str):
                sloz_umnoz(Matrix, Free, r, str, -1 * Matrix[r][stl_max], len(Matrix[str]))

        str = str + 1








print("About first LO")
print("Number of vectors")
n1 = int(input())
print("Amount of coords")
m1 = int(input())

A = []

for i in range(n1):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    A.append(row)


realA = [[0.0] * len(A[0]) for i in range(len(A))]


for i in range(len(realA)):
    for j in range(len(realA[i])):
        realA[i][j] = A[i][j]


b = [0] * len(A)

Gauss(realA, b)
solutions = [0] * len(realA[0])

k = 0
x = 0
for r in range(len(realA)):
    for l in range(len(realA[r])):
        if realA[r][l] == 0:
            k = k + 1
    # print(k)
    if k == len(realA[0]):
        # print(k)
        x = x + 1
    k = 0

rg = len(realA) - x




print("=================dim L1=================")
print(rg)
print("=================bazis L1=================")
for i in range(rg):
    print(A[i])


print("About second LO")
print("Number of vectors")
n2 = int(input())
print("Amount of coords")
m2 = int(input())
if m1!=m2:
    print("STOP IT!!!!")
B = []

for i in range(n2):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    B.append(row)


realB = [[0.0] * len(B[0]) for i in range(len(B))]


for i in range(len(realB)):
    for j in range(len(realB[i])):
        realB[i][j] = B[i][j]


b1 = [0] * len(B)

Gauss(realB, b1)
solutions1 = [0] * len(realB[0])

k = 0
x = 0
for r in range(len(realB)):
    for l in range(len(realB[r])):
        if realB[r][l] == 0:
            k = k + 1
    # print(k)
    if k == len(realB[0]):
        # print(k)
        x = x + 1
    k = 0

rg2 = len(realB) - x




print("=================dim L2=================")
print(rg2)
print("=================bazis L2=================")
for i in range(rg2):
    print(B[i])
    
    
    
    
C = []

for i in range(n1):
    C.append(A[i])
  
for i in range(n2):
    C.append(B[i])

#printM(C)
  
realC = [[0.0] * len(C[0]) for i in range(len(C))]


for i in range(len(realC)):
    for j in range(len(realC[i])):
        realC[i][j] = C[i][j]


b2 = [0] * len(C)

Gauss(realC, b2)
solutions2 = [0] * len(realC[0])

k = 0
x = 0
for r in range(len(realC)):
    for l in range(len(realC[r])):
        if realC[r][l] == 0:
            k = k + 1
    # print(k)
    if k == len(realC[0]):
        # print(k)
        x = x + 1
    k = 0

rg3 = len(realC) - x




print("=================dim L1 + L2=================")
print(rg3)
print("=================bazis L1 + L2=================")
for i in range(rg3):
    print(C[i])
 
 
 
dimL1L2 = rg + rg2 - rg3  
  
print("=================dim L1 || L2=================")
print(dimL1L2)
print("=================bazis L1 || L2=================")
if dimL1L2 == rg:
    for i in range(rg):
        print(A[i])
 
elif dimL1L2 == rg2:
    for i in range(rg2):
        print(B[i])       
        
elif dimL1L2 == 0:
    print("================PRYAMAYA SUMMA=================")

else:    
    D = []

    for i in range(rg):
        D.append(A[i])
  
    for i in range(rg2):
        D.append(B[i])        
        

    for i in range(dimL1L2):
        print(D[i])    
