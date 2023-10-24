import matplotlib.pyplot as plt

Gwei = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
Price = [0.2071,0.41419,0.62129,0.82838,1.03548,1.24258,1.44967,1.65677,1.86386,2.07096]
USDcost = [321.31,642.6,963.91,1285.2,1606.51,1927.81,2249.11,2570.41,2891.7,3213.01]

# plot line graph
plt.plot(Gwei, Price, marker='o', label='Price')
plt.plot(Gwei, USDcost, marker='o', label='USD cost')

# set axis label
plt.xlabel('Gwei')
plt.ylabel('Price & USD cost')

# set legend
plt.legend()

# show plot
plt.show()