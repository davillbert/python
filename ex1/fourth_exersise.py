class Complex():
    count = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Complex.count += 1
    def compare(self, a1, b1, a2, b2):
        if (a1 == a2) and (b1 == -b2):
            print('\nNumbers are conjugate')
        else:
            print('\nNumbers are not conjugate')


C1 = Complex(3,1)
C2 = Complex(2,-1)
C1.compare(C1.a, C1.b, C2.a, C2.b)