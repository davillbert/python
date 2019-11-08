class Circle():
    count = 0
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R
        if (self.R < 0):
            print ('It is a mistake')
            self.R = -1 * self.R
        else:
            self.R = R
        Circle.count += 1

    def square(self, R):
        return self.R * self.R

    def compare(self, S1, S2):
        if (S1 == S2):
            print('Squres are same')
        else:
            print('Squares are different')

C1 = Circle(0,0,12)
square_C1 = C1.square(12)

C2 = Circle(3,5,11)
square_C2 = C2.square(11)

C1.compare(square_C1, square_C2)






