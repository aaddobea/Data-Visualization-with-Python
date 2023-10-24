import numpy as np
import matplotlib.pyplot as plt

schemes = {
    'IC-CHS': [1480000, 2800000, 4040000, 5520000, 6900000, 8480000],
    'NP-IoT': [1823000, 3646000, 5469000, 7292000, 9115000, 10938000],
    'IH-IoT': [1586000, 3172000, 4758000, 6344000, 7930000, 9516000],
    'Proposed': [252000, 504000, 756000, 1008000, 1260000, 1512000]
}

# create a figure and axis
fig, ax = plt.subplots()

# plot the lines with markers
ax.plot(schemes['IC-CHS'], label='IC-CHS', marker='o')
ax.plot(schemes['NP-IoT'], label='NP-IoT', marker='x')
ax.plot(schemes['IH-IoT'], label='IH-IoT', marker='s')
ax.plot(schemes['Proposed'], label='Proposed', marker='*')

# set the title and axis labels
ax.set_title('Comparison of IoT Networks')
ax.set_xlabel('schemes')
ax.set_ylabel('Transaction computation cost')

# add a legend and grid
ax.legend()
ax.grid(True)

# show the plot
plt.show()