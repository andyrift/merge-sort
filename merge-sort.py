import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("error")

matplotlib.rcParams.update({'font.size': 16})

def Read(folder):

    x=[]
    for i in range(10):
        f = open('%s/out%d.txt'%(folder, i), "r")
        x.append(f.read())
        f.close()
        x[i] = x[i].split(" ")
        x[i].pop()
        for j in range(len(x[i])):
            x[i][j] = x[i][j].split("/")

    N = []
    T = []
    for i in range(10):
        N.append([int(pair[0]) for pair in x[i]])
        T.append([int(pair[1]) for pair in x[i]])

    n = N[0]

    L = [oneN * np.log2(oneN) for oneN in n]

    approx = []
    for t in T:
        for i in range(10, len(t)):
            approx.append(t[i]/L[i])
    approx = np.mean(approx)

    Lapprox = [approx * l for l in L]

    ratapprox = [2+2/np.log2(oneN) for oneN in n]

    ratapprox.pop()

    return x, N, T, n, approx, L, Lapprox, ratapprox

x, N, T, n, approx, L, Lapprox, ratapprox = Read("2")

#----------------------------------------------------------------------

fig1 = plt.figure('Tests 1', figsize=(16, 9), dpi=80)
fig1.suptitle('Testing with array length n = 2^i', fontsize=20)

ax = fig1.add_subplot(1, 2, 1)
ax.set_title("Time for each test")

ax.set_xscale('log')
ax.set_yscale('log')

ax.grid(True)

for i in range(10):
    plt.plot(n, T[i], '-', label='Test %d'%i)

plt.plot(n, Lapprox, ':', label='%f*n*log_2(n)'%approx)

ax.legend()

plt.xticks(ticks=n, labels=n, rotation=90)

plt.xlabel("Array length: n")
plt.ylabel("Time in nanoseconds")

#-----------------------------------------------------------------------------------------
ax = fig1.add_subplot(1, 2, 2)
ax.set_title("Average time for each array length between tests")

ax.set_xscale('log')
ax.set_yscale('log')

ax.grid(True)

avg = []
for i in range(len(n)):
    tmp = []
    for t in T:
        tmp.append(t[i])
    avg.append(np.mean(tmp))
    
plt.plot(n, avg, '-', label='Average')

plt.plot(n, Lapprox, ':', label='%f*n*log_2(n)'%approx)

ax.legend()

plt.xticks(ticks=n, labels=n, rotation=90)

plt.xlabel("Array length: n")
plt.ylabel("Time in nanoseconds")

#------------------------------------------------------------------------------------------

rat = []

for i in range(1, len(avg)):
    rat.append(avg[i]/avg[i-1])

fig3 = plt.figure('Ratios', figsize=(16, 9), dpi=80)
fig3.suptitle('Ratios', fontsize=20)

ax = fig3.add_subplot(1, 2, 1)
ax.set_title("n = 2^i")

#ax.set_xscale('log')
#ax.set_yscale('log')

ax.grid(True)
    
plt.plot(range(len(rat)), rat, '-', label='Ratio')

plt.plot(range(len(rat)), ratapprox, '-.', label='2+2/log_2(n)')

ax.legend()

xs = range(len(rat))

labels = ["T (2^"+str(xss+2)+") / T (2^"+str(xss+1)+")" for xss in xs]

plt.xticks(ticks=range(len(rat)), labels=labels, rotation=45, ha="right")

plt.xlabel("Adjacent measurements")
plt.ylabel("Ratio of two adjacent measurements")


#------------------------------------------------------------------------------------------

x, N, T, n, approx, L, Lapprox, ratapprox = Read("3")

#----------------------------------------------------------------------

fig2 = plt.figure('Tests 2', figsize=(16, 9), dpi=80)
fig2.suptitle('Testing with array length n = 3*2^i', fontsize=20)

ax = fig2.add_subplot(1, 2, 1)
ax.set_title("Time for each test")

ax.set_xscale('log')
ax.set_yscale('log')

ax.grid(True)

for i in range(10):
    plt.plot(n, T[i], '-', label='Test %d'%i)

plt.plot(n, Lapprox, ':', label='%f*n*log_2(n)'%approx)

ax.legend()

plt.xticks(ticks=n, labels=n, rotation=90)

plt.xlabel("Array length: n")
plt.ylabel("Time in nanoseconds")

#-----------------------------------------------------------------------------------------
ax = fig2.add_subplot(1, 2, 2)
ax.set_title("Average time for each array length between tests")

ax.set_xscale('log')
ax.set_yscale('log')

ax.grid(True)

avg = []
for i in range(len(n)):
    tmp = []
    for t in T:
        tmp.append(t[i])
    avg.append(np.mean(tmp))
    
plt.plot(n, avg, '-', label='Average')

plt.plot(n, Lapprox, ':', label='%f*n*log_2(n)'%approx)

ax.legend()

plt.xticks(ticks=n, labels=n, rotation=90)

plt.xlabel("Array length: n")
plt.ylabel("Time in nanoseconds")

#------------------------------------------------------------------------------------------

rat = []

for i in range(1, len(avg)):
    rat.append(avg[i]/avg[i-1])

fig3 = plt.figure(num="Ratios")

ax = fig3.add_subplot(1, 2, 2)
ax.set_title("n = 3*2^i")

ax.grid(True)
    
plt.plot(range(len(rat)), rat, '-', label='Ratio')

plt.plot(range(len(rat)), ratapprox, '-.', label='2+2/log_2(n)')

ax.legend()

xs = range(len(rat))

labels = ["T (3*2^"+str(xss+1)+") / T (3*2^"+str(xss)+")" for xss in xs]

plt.xticks(ticks=range(len(rat)), labels=labels, rotation=45, ha="right")

plt.xlabel("Adjacent measurements")
plt.ylabel("Ratio of two adjacent measurements")

#------------------------------------------------------------------------------------------

plt.show()
