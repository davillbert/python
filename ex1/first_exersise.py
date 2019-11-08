class Little_child():
    noise = 17
    def change_noise(self):
        return self.noise
    def __init__(self, name):
        self.name = name
    def how_much(self, time):
        print('\n ', self.name,
              'is cry still ',  self.change_noise() + time, ' hours')
this_child = Little_child('Boris')
noisy_time = this_child.change_noise()
print(noisy_time)
this_child.how_much(23)


