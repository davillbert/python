A = [
    [3, -6, 9, 13, 0, 7],
    [-1,2,1,1, 0, 8],
    [1,-2,2,3, 1, 1]
]

b = [0, 0, 0]

def umnozhit(Matrix, Free, str, number, n):
    for j in range(n):
        if (Matrix[str][j] == int(Matrix[str][j])):
            Matrix[str][j] = Matrix[str][j] * number
        else:
            Matrix[str][j] = round(Matrix[str][j] * number , 15)
    if (Free[str] == int(Free[str])):
        Free[str] = Free[str] * number
    else:
        Free[str] = round(Free[str] * number , 15)


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

Gauss(A, b)

k = 0
x = 0
for r in range(len(A)):
    for l in range(len(A[r])):
        if A[r][l] == 0.00000:
            k = k + 1
    if k == len(A[r]):
        x = x + 1
        print(k, " ", x)
        k = 0

rg = len(A) - x

print("================rg================")
print(rg)

print("================A================")
printM(A)
print("================b================")
printF(b)

N = len(A[0])
M = len(A[0]) - rg
F = [[0.0] * M for i in range(N)]

for i in range(rg):
    for j in range(M):
        F[i][j] = - A[i][j + len(A[0]) - rg]

for i in range(rg, N):
    for j in range(M):
        if (i - rg == j):
            F[i][j] = 1.0


