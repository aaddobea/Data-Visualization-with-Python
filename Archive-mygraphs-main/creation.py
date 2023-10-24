import matplotlib.pyplot as plt
import numpy as np

data_size = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
aes_encryption = [0.0000251, 0.0000271, 0.0000292, 0.0000312, 0.0000331, 0.0000352, 0.0000372, 0.0000393, 0.0000412, 0.0000432]
mac = [0.000013, 0.000014, 0.000015, 0.000016, 0.000017, 0.000018, 0.000018, 0.000019, 0.000020, 0.000021]
signcryption = [6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7, 6.7e-7]


fig, ax = plt.subplots(figsize=(10,5), dpi=100)

# Data Creation
data_creation = np.add(np.add(aes_encryption, mac), signcryption)
print(data_creation)
ax.plot(data_size, aes_encryption, label='AES Encryption', color='darkblue', marker='o')
ax.plot(data_size, mac, label='MAC', color='green', marker='o')
ax.plot(data_size, signcryption, label='Signcryption', color='red', marker='o')
ax.plot(data_size, data_creation, label='Data creation', color='purple', marker='o')
ax.legend(loc='upper left')

# Additional plot formatting
ax.set_xlabel('Data size (MB)')
ax.set_ylabel('Time (seconds)')


# ax.set_title('Encryption/Decryption Time Comparison')
ax.set_xticks(data_size)
ax.set_xticklabels(data_size, rotation=45)
ax.grid(visible=True, which='both', axis='both', linewidth=0.5, linestyle='-.', alpha=0.7, color='black')

#loc="/Users/Isaac/Downloads/core-master/vcode/data/DataCreation.jpg"
#loc="/C:\Users\abiga\Documents\KEY encap conference"
#plt.savefig(loc, dpi=500, bbox_inches='tight')

plt.show()
