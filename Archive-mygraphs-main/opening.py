import matplotlib.pyplot as plt
import numpy as np

data_size = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
aes_decryption = [0.000025, 0.000027, 0.000029, 0.000031, 0.000033, 0.000035, 0.000037, 0.000039, 0.000041, 0.000043]
mac = [0.000013, 0.000014, 0.000015, 0.000016, 0.000017, 0.000018, 0.000018, 0.000019, 0.000020, 0.000021]
unsigncryption = [4.51e-7, 4.52e-7, 4.51e-7, 4.52e-7, 4.51e-7, 4.53e-7, 4.54e-7, 4.51e-7, 4.51e-7, 4.51e-7]

fig, ax = plt.subplots(figsize=(10,5))

# Data Creation
data_creation = np.add(np.add(aes_decryption, mac), unsigncryption)
print(data_creation)
ax.plot(data_size, aes_decryption, label='AES Decryption', color='darkblue', marker='o')
ax.plot(data_size, mac, label='MAC', color='green', marker='o')
ax.plot(data_size, unsigncryption, label='Unsigncryption', color='red', marker='o')
ax.plot(data_size, data_creation, label='Data Opening', color='purple', marker='o')
ax.legend(loc='upper left')

# Additional plot formatting
ax.set_xlabel('Data size (MB)')
ax.set_ylabel('Time (Seconds)')
#ax.set_title('Encryption/Decryption Time Comparison')
ax.set_xticks(data_size)
ax.set_xticklabels(data_size, rotation=45)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')


#loc="/Users/Isaac/Downloads/core-master/vcode/data/DataOpening.jpg"
#plt.savefig(loc, dpi=500, bbox_inches='tight')
plt.show()
