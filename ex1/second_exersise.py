def how_much(self, time):
    print('\n ', self.name,
          'is cry still ', self.change_noise() + time, ' hours')

class Little_child():
    noise = 17
    def change_noise(self):
        return self.noise
    def __init__(self, name):
        self.name = 'Sergey'
    how_much_class = how_much

this_child = Little_child('Boris')
noisy_time = this_child.change_noise()
print(noisy_time)
this_child.how_much_class(23)

not_this_child = Little_child('')
noisy_time = not_this_child.change_noise()
not_this_child.how_much_class(3)

not_this_child.noise = 90
print(not_this_child.noise)
print(noisy_time)