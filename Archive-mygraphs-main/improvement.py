import matplotlib.pyplot as plt

requests = [200, 400, 800, 1200, 2400, 4800, 9600]
time1 = [0.03, 0.06, 0.12, 0.18, 0.36, 0.72, 1.44]
time2 = [0.189, 0.408, 0.816, 1.224, 2.448, 4.896, 9.792]
total = [0.219, 0.468, 0.936, 1.404, 2.808, 5.616, 11.232]

plt.plot(requests, time1, marker='o', linestyle='--', color='r', label='Time 1')
plt.plot(requests, time2, marker='s', linestyle='-.', color='g', label='Time 2')
plt.plot(requests, total, marker='^', linestyle=':', color='b', label='Total')
plt.xlabel('Requests')
plt.ylabel('Time (seconds)')
plt.xscale('log')
plt.grid()
plt.title("Graph of Requests vs Time")
plt.legend()
plt.show()
