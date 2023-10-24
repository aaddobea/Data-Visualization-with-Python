import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.colors as mcolors
#print(plt.style.available)
plt.style.use('ggplot')

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ic_chs_non_zero = [0.00074, 0.00148, 0.00222, 0.00295, 0.00369, 0.00443, 0.00517, 0.00591, 0.00665, 0.00738]
np_iot_non_zero = [0.00035, 0.00071, 0.00106, 0.00142, 0.00177, 0.00212, 0.00248, 0.00283, 0.00319, 0.00354]
ih_iot_non_zero = [0.00024, 0.00048, 0.00072, 0.00096, 0.00121, 0.00145, 0.00169, 0.00193, 0.00217, 0.00241]
proposed_non_zero = [0.00022, 0.00044, 0.00066, 0.00087, 0.00109, 0.00131, 0.00153, 0.00175, 0.00191, 0.00213]
ic_chs_zero = [0.00033, 0.00066, 0.001, 0.00133, 0.00166, 0.00199, 0.00233, 0.00266, 0.00299, 0.00332]
np_iot_zero = [0.00025, 0.00051, 0.00076, 0.00101, 0.00127, 0.00152, 0.00177, 0.00203, 0.00228, 0.00254]
ih_iot_zero = [0.00022, 0.00043, 0.00065, 0.00087, 0.00109, 0.00131, 0.00153, 0.00175, 0.00197, 0.00218]
proposed_zero = [0.00021, 0.00043, 0.00064, 0.00085, 0.00106, 0.00128, 0.00149, 0.0017, 0.00191, 0.00213]




# plot the data using matplotlib
bar_width = 0.2
x_pos = np.arange(len(x))

fig, ax = plt.subplots()
ax.bar(x_pos, ic_chs_zero, bar_width, align='center', color='dodgerblue', label='IC-CHS')
#ax.bar(x_pos, ic_chs_non_zero, bar_width, align='center', color='dodgerblue', label='IC-CHS Non-zero')
ax.bar(x_pos + bar_width, np_iot_zero, bar_width, align='center',color='orange', label='NP-IoT')
#ax.bar(x_pos + bar_width, np_iot_non_zero, bar_width, align='center',color='orange', label='NP-IoT Non-zero')
ax.bar(x_pos + 2*bar_width, ih_iot_zero, bar_width, align='center', color='lime', label='IH-IoT')
#ax.bar(x_pos + 2*bar_width, ih_iot_non_zero, bar_width, align='center', color='lime', label='IH-IoT Non-zero')
ax.bar(x_pos + 3*bar_width, proposed_zero, bar_width, align='center', color='magenta', label='Proposed')
#ax.bar(x_pos + 3*bar_width, proposed_non_zero, bar_width, align='center', color='magenta', label='Proposed Non-zero')

#fig, ax = plt.subplots()
ax.bar(x_pos, ic_chs_non_zero, bar_width, align='center', color='dodgerblue', label='IC-CHS Non-zero')
ax.bar(x_pos + bar_width, np_iot_non_zero, bar_width, align='center',color='orange', label='NP-IoT Non-zero')
ax.bar(x_pos + 2*bar_width, ih_iot_non_zero, bar_width, align='center', color='lime', label='IH-IoT Non-zero')
ax.bar(x_pos + 3*bar_width, proposed_non_zero, bar_width, align='center', color='magenta', label='Proposed Non-zero')



plt.xlabel('Data Points in Gwei')
plt.ylabel('Value')
plt.title('Graph')

plt.legend()

plt.show()