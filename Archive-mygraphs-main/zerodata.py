import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# define the data
x = [10,20,30,40,50,60,70,80,90,100]
ic_chs = [0.00024,0.00048,0.00072,0.00096,0.00121,0.00145,0.00169,0.00193,0.00217,0.00241]
np_iot = [0.00022,0.00043,0.00065, 0.00087, 0.00109,0.0013, 0.00152, 0.00174, 0.00195, 0.00217]
ih_iot = [0.00022,0.00044, 0.00066, 0.00087, 0.00109, 0.00131,0.00153,0.00175, 0.00197,0.00218]
proposed = [0.00021,0.00043,0.00064,0.00085,0.00106,0.00128,0.00149,0.0017,0.00191,0.00213]

# plot the data using matplotlib
bar_width = 0.2
x_pos = np.arange(len(x))

fig, ax = plt.subplots()
ax.bar(x_pos, ic_chs, bar_width, align='center', color='darkorange', label='IC-CHS')
ax.bar(x_pos + bar_width, np_iot, bar_width, align='center',color='red', label='NP-IoT')
ax.bar(x_pos + 2*bar_width, ih_iot, bar_width, align='center', label='IH-IoT')
ax.bar(x_pos + 3*bar_width, proposed, bar_width, align='center', color='fuchsia', label='Proposed')
#ax.grid(alpha=0.8)

# add labels and title
plt.xlabel('Gwei')
plt.ylabel('Total transaction cost')
plt.title('Total transaction cost for zero byte transaction data')

# add xticks and legend
plt.xticks(x_pos + bar_width, x)
plt.legend()
plt.savefig('zerodata.png')

# show the plot
plt.show()