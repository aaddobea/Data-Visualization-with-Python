import matplotlib.pyplot as plt
import numpy as np

data_size = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
aes_decryption = [0.000025, 0.000027, 0.000029, 0.000031, 0.000033, 0.000035, 0.000037, 0.000039, 0.000041, 0.000043]
mac = [0.000013, 0.000014, 0.000015, 0.000016, 0.000017, 0.000018, 0.000018, 0.000019, 0.000020, 0.000021]
unsigncryption = [4.51e-7, 4.52e-7, 4.51e-7, 4.52e-7, 4.51e-7, 4.53e-7, 4.54e-7, 4.51e-7, 4.51e-7, 4.51e-7]



fig, ax = plt.subplots(figsize=(10,5))

# Data Creation
ax.bar(data_size, aes_decryption, label='AES Decryption', color='darkblue')
ax.bar(data_size, mac, label='MAC', bottom=aes_decryption, color='green')
ax.bar(data_size, unsigncryption, label='unsigncryption', bottom=np.add(aes_decryption,mac), color='red')
ax.legend(loc='upper left')

# Additional plot formatting
ax.set_xlabel('Data size (MB)')
ax.set_ylabel('Time (ms)')
# #ax.set_title('Encryption/Decryption Time Comparison')
ax.set_xticks(data_size)
ax.set_xticklabels(data_size, rotation=45)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')



fig, ax = plt.subplots(figsize=(10,5))

# Data Creation
data_creation = np.add(np.add(aes_decryption, mac), unsigncryption)
ax.plot(data_size, aes_decryption, label='AES Decryption', color='darkblue', marker='o')
ax.plot(data_size, mac, label='MAC', color='green', marker='o')
ax.plot(data_size, unsigncryption, label='Unsigncryption', color='red', marker='o')
ax.plot(data_size, data_creation, label='Data Opening', color='purple', marker='o')
ax.legend(loc='upper left')

# Additional plot formatting
ax.set_xlabel('Data size (MB)')
ax.set_ylabel('Time (ms)')
#ax.set_title('Encryption/Decryption Time Comparison')
ax.set_xticks(data_size)
ax.set_xticklabels(data_size, rotation=45)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')


fig, ax = plt.subplots(figsize=(10,5))

# Data Creation
data_creation = np.add(np.add(aes_decryption, mac), unsigncryption)
aes_decryption_percent = np.divide(aes_decryption, data_creation) * 100
mac_percent = np.divide(mac, data_creation) * 100
unsigncryption_percent = np.divide(unsigncryption, data_creation) * 100

# Plotting
ax.bar(data_size, aes_decryption_percent, label='AES Decryption', color='darkblue')
ax.bar(data_size, mac_percent, label='MAC', bottom=aes_decryption_percent, color='green')
ax.bar(data_size, unsigncryption_percent, label='Unsigncryption', bottom=np.add(aes_decryption_percent,mac_percent), color='red')
ax.legend(loc='upper left')

# Additional plot formatting
ax.set_xlabel('Data size (MB)')
ax.set_ylabel('Percentage(%)')
# ax.set_title('Encryption/Decryption Time Comparison in Percentage')
ax.set_xticks(data_size)
ax.set_xticklabels(data_size, rotation=45)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')


fig, ax = plt.subplots(figsize=(10,5))

# Data Creation
data_creation = np.add(np.add(aes_decryption, mac), unsigncryption)
aes_decryption_percent = np.divide(aes_decryption, data_creation) * 100
mac_percent = np.divide(mac, data_creation) * 100
unsigncryption_percent = np.divide(unsigncryption, data_creation) * 100

# Plotting
ax.bar(data_size, aes_decryption_percent, label='AES Decryption', color='darkblue')
ax.bar(data_size, mac_percent, label='MAC', bottom=aes_decryption_percent, color='green')
ax.bar(data_size, unsigncryption_percent, label='Unsigncryption', bottom=np.add(aes_decryption_percent,mac_percent), color='red')
ax.legend(loc='upper left', bbox_to_anchor=(0.01, 1.005))

# Additional plot formatting
ax.set_xlabel('Data (MB)', fontsize=12)
ax.set_ylabel('Percentage(%)', fontsize=12)
# ax.set_title('Encryption/Decryption Time Comparison in Percentage', fontsize=14)
ax.set_xticks(data_size)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_xticklabels(data_size, rotation=45, fontsize=12)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')
ax.axhline(100, color='black', linewidth=1)
ax.axhline(0, color='black', linewidth=1)
ax.set_ylim(0, 111)

# Adding label above each bar
for i in range(len(data_size)):
    ax.text(x = data_size[i] - 7, y = aes_decryption_percent[i]-20, s = f'{aes_decryption_percent[i]:.2f}%', size = 8)
    ax.text(x = data_size[i] - 7, y = aes_decryption_percent[i]-14 + mac_percent[i] + 2, s = f'{mac_percent[i]:.2f}%', size = 8)
    ax.text(x = data_size[i] - 7, y = aes_decryption_percent[i]-3.8 + mac_percent[i]+ unsigncryption_percent[i] + 2, s = f'{unsigncryption_percent[i]:.2f}%', size = 8)
    
# Adding caption 
plt.show()

plt.show()
