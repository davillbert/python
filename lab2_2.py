import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline
f = open('/home/davillbert/Documents/ded/signals/signal01.dat', 'r')
nums = []
f.readline()
for line in f:
        nums.append(line.split())
chiselki = []
for i in nums:
    chiselki.append(i[0])
x = []
for i in range(len(chiselki)):
    x.append(i)
y1 = [float(j) for j in chiselki]

def p(a, num):
    s = 0
    k = 0
    for i in a:
        if k <= num:
            s = s + i
            k = k + 1
    return s
y2 = []
y2.append(y1[0])
for i in range(len(y1)):
    y2.append((p(y2,i) + y1[i])/(i+1))
del y2[0]

fg = plt.figure(figsize=(10, 7))
gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fg)

fig_ax_1 = fg.add_subplot(gs[0, 0])
plt.plot(x, y1, label='linear', marker='', linestyle='-', color='blue', linewidth=1)
plt.legend()
fig_ax_2 = fg.add_subplot(gs[0, 1])
plt.plot(x, y2)


plt.show()
