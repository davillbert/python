import matplotlib.pyplot as plt
%matplotlib inline
#f = open('/home/davillbert/Documents/ded/signals/signal01.dat')
#data = np.array(f) 
def p(a, num):
    s = 0
    k = 0
    for i in a:
        if k <= num:
            s = s + i
            k = k + 1
    return s
        
        
data = np.genfromtxt('/home/davillbert/Documents/ded/signals/signal01.dat')
#p = int(data[0])
data2 = np.fromfunction(lambda i: (p(data2,i) + data[i])/(i+1), (data.size,), dtype = int)
#data2 = np.array()
#data2[0] = int(data[0])
#for i in range(1, data.size):
   # data2.append((p + int(data[i]))/(i+1))
   # p = p + int(data2[i])
   # print(data2[i])

"""
fg = plt.figure(figsize=(14, 7))
gs = gridspec.GridSpec(ncols=1, nrows=1, figure=fg)

fig_ax_1 = fg.add_subplot(gs[0, 0])
plt.plot(x, y1, label='linear', marker='o', linestyle=' ', color='blue', linewidth=2)
plt.legend()


plt.show()
"""
print(data)
print(data2)
