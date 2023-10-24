import matplotlib.pyplot as plt

# Data
gwei = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
nonzero_price = [0.00074, 0.00148, 0.00222, 0.00295, 0.00369, 0.00443, 0.00517, 0.00591, 0.00665, 0.00738]
zero_price = [0.00024, 0.00048, 0.00072, 0.00096, 0.00121, 0.00145, 0.00169, 0.00193, 0.00217, 0.00241]

# Plot
plt.plot(gwei, zero_price, label='zero', color='blue', marker='>',linestyle = 'dashed')
plt.plot(gwei, nonzero_price, label='non-zero',color='deeppink',marker='v',linestyle = 'dashed')
#plt.plot(label = "line graph", color = 'red', marker = "o", linestyle = 'dashed', linewidth = 3, markersize = 10)
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')

# Add labels and title
plt.xlabel('Gwei')
plt.ylabel('Transaction Price')
plt.title('Total transaction cost for zero and non-zero prices for IC-CHS')

# Add legend
plt.legend()
plt.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')


#loc="/Users/Isaac/Downloads/core-master/vcode/data/DataCreation.jpg"
#loc="C:\Users\abiga\Downloads\Archive\IC-CHS limit.jpg"
#plt.savefig(loc, dpi=500, bbox_inches='tight')
plt.savefig('IC-CHS.png')
# Show plot
plt.show()
