A = [
    [1, 2, 3],  # 0 0 = 1     0 1 = 2     0 2 = 3
    [4, 5, 6],  ## 1 0 = 4     1 1 = 5    1 1 = 6
    [7, 8, 9]  # 2 0 = 7    2 1 = 8   2 2 = 9
]

b = [1, 1, 1]


# 1 - умножение на чиселку
# 2 - перестановка
# 3 - сложение
# 1) и 3)
# 4 - вывод на экран

def umnozhit(Matrix, Free, str, number, n):
    for j in range(n):
        Matrix[str][j] = Matrix[str][j] * number
    Free[str] = Free[str] * number


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


def Gauss(Matrix, Free, n):
    str = 0
    while (str < n):
        stl_max = -1
        for r in range(n):
            if (Matrix[str][r] != 0):
                stl_max = r
        if (stl_max == -1):
            print("No solutions")
        # return 0

        umnozhit(Matrix, Free, str, 1 / Matrix[str][stl_max], n)

        for r in range(n):
            if(r!=str):
                sloz_umnoz(Matrix, Free, r, str, -1 * Matrix[r][stl_max], n)

        if (stl_max != str):
            perestanovka(Matrix, Free, stl_max, str)

        str = str + 1


Gauss(A, b, 3)

print("================A================")
printM(A)
print("================b================")
printF(b)
