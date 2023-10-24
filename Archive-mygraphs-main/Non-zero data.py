import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# define the data
x = [10,20,30,40,50,60,70,80,90,100]
ic_chs = [0.00074,0.00148,0.00222,0.00295,0.00369,0.00443,0.00517,0.00591,0.00665,0.00738]
np_iot = [0.00033,0.00066,0.001,0.00133,0.00166,0.00199,0.00233,0.00266,0.00299,0.00332]
ih_iot = [0.00035,0.00071,0.00106,0.00142,0.00177,0.00212,0.00248,0.00283,0.00319,0.00354]
proposed = [0.00025,0.00051,0.00076,0.00101,0.00127,0.00152,0.00177,0.00203,0.00228,0.00254]

# plot the data using matplotlib
bar_width = 0.2
x_pos = np.arange(len(x))

fig, ax = plt.subplots(figsize=(6 ,5), dpi=100)
ax.bar(x_pos, ic_chs, bar_width, align='center', color='dodgerblue', label='IC-CHS')
ax.bar(x_pos + bar_width, np_iot, bar_width, align='center', label='NP-IoT')
ax.bar(x_pos + 2*bar_width, ih_iot, bar_width, align='center', color='lime', label='IH-IoT')
ax.bar(x_pos + 3*bar_width, proposed, bar_width, align='center', color='magenta', label='Proposed')
#ax.grid(alpha=0.8)

# add labels and title
plt.xlabel('Gwei')
plt.ylabel('Total transaction cost')
plt.title('Total transaction cost for non-zero transaction data')

# add xticks and legend
plt.xticks(x_pos + bar_width, x)
plt.legend()
plt.savefig('Non-zero data.png')


# show the plot
plt.show()