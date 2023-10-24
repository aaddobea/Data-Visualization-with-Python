import matplotlib.pyplot as plt
import numpy as np


# Create lists for the number of requests and the corresponding time taken
requests = [200, 400, 800, 1200, 2400, 4800, 9600, 19200, 38400, 76800, 153600, 307200, 614400, 1228800, 2457600, 4915200, 9830400, 19668000]
times = [0.03, 0.06, 0.12, 0.18, 0.36, 0.72, 1.44, 2.88, 5.76, 11.52, 23.04, 46.08, 92.16, 184.32, 368.64, 737.28, 1474.56, 2950.2]

# Create the line graph and add gridlines
plt.plot(requests, times, 'bo-',label="Data",linewidth=2)
plt.grid(True)

# Add a logarithmic scale to the x-axis
plt.xscale('log')

# Add labels for each data point
for i, txt in enumerate(requests):
    plt.annotate(txt, (requests[i], times[i]),fontsize = 8,rotation=65,bbox=dict(boxstyle="square,pad=0.002", fc="white", ec="b", lw=0.08,alpha=0.4))


# Add a trendline to the graph
coefficients = np.polyfit(requests, times, 1)
trendline = np.poly1d(coefficients)
plt.plot(requests, trendline(requests), 'r-',label="Trendline")

# Add horizontal line to represent the average time
average_time = sum(times) / len(times)
plt.axhline(average_time, color='g', linestyle='--', label='Average Time')

# Add legend to the graph
plt.legend(loc='upper left')

# Add labels and title with bigger font size
plt.xlabel('Number of Requests')
plt.ylabel('Server Throughput (Re-encryption/ms)')
# plt.title('Performance of the System',size=20)
#loc="/Users/Isaac/Downloads/core-master/vcode/data/Re-encryption.jpg"
#plt.savefig(loc, dpi=500, bbox_inches='tight')

# Provide better layout for the graph
plt.figure(figsize=(12,8))
plt.ylim(0,35)
# Save the figure

# Show the graph
plt.show()
