import matplotlib.pyplot as plt

# Data
gwei = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
nonzero_price = [0.00025, 0.00051, 0.00076, 0.00101, 0.00127, 0.00152, 0.00177, 0.00203, 0.00228, 0.00254]
zero_price = [0.00021, 0.00043, 0.00064, 0.00085, 0.00106, 0.00128, 0.00149, 0.0017, 0.00191, 0.00213]

# Plot
plt.plot(gwei, zero_price, label='zero', color='royalblue', marker='v',linestyle = 'dashed')
plt.plot(gwei, nonzero_price, label='non-zero',color='darkorange',marker='s',linestyle = 'dashed')
#plt.plot(label = "line graph", color = 'red', marker = "o", linestyle = 'dashed', linewidth = 3, markersize = 10)
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')

# Add labels and title
plt.xlabel('Gwei')
plt.ylabel('Transaction Price')
plt.title('Total transaction cost for zero and non-zero prices for Proposed')

# Add legend
plt.legend()
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')
plt.savefig('Proposed.png')

# Show plot
plt.show()