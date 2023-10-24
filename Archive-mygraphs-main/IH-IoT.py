import matplotlib.pyplot as plt

# Data
gwei = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
nonzero_price = [0.00035, 0.00071, 0.00106, 0.00142, 0.00177, 0.00212, 0.00248, 0.00283, 0.00319, 0.00354]
zero_price = [0.00022,0.00044, 0.00066,0.00087, 0.00109, 0.00131,0.00153, 0.00175, 0.00197, 0.00218]

# Plot
plt.plot(gwei, zero_price, label='zero', color='tomato', marker='p',linestyle = 'dashed')
plt.plot(gwei, nonzero_price, label='non-zero',color='mediumblue',marker='*',linestyle = 'dashed')
#plt.plot(label = "line graph", color = 'red', marker = "o", linestyle = 'dashed', linewidth = 3, markersize = 10)
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')

# Add labels and title
plt.xlabel('Gwei')
plt.ylabel('Transaction Price')
plt.title('Total transaction cost for zero and non-zero prices for IH-IoT')

# Add legend
plt.legend()
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')
plt.savefig('IH-IoT.png')

# Show plot
plt.show()