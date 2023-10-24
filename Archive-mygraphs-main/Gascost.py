import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Data
user_key_gen = [('IC-CHS', 36600), ('NP-IoT', 6000), ('IH-IoT', 79000), ('Proposed', 12000)]
encap = [('IC-CHS', 91300), ('NP-IoT', 103150), ('IH-IoT', 12300), ('Proposed', 30600)]
decap = [('IC-CHS', 79000), ('NP-IoT', 91150), ('IH-IoT', 79300), ('Proposed', 12600)]
total = [('IC-CHS', 206900), ('NP-IoT', 200300), ('IH-IoT', 170600), ('Proposed', 55200)]

# Extract labels and values for each group
labels = [x[0] for x in user_key_gen]
user_key_gen_values = [x[1] for x in user_key_gen]
encap_values = [x[1] for x in encap]
decap_values = [x[1] for x in decap]
total_values = [x[1] for x in total]

# Set width of each bar
bar_width = 0.2

# Set positions of bars on x-axis
r1 = range(len(user_key_gen_values))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Plot histogram
plt.bar(r1, user_key_gen_values, color='lime', width=bar_width, label='PKeyGen')
plt.bar(r2, encap_values, color='deeppink', width=bar_width, label='Encap')
plt.bar(r3, decap_values, color='blue', width=bar_width, label='Decap')
plt.bar(r4, total_values, color='magenta', width=bar_width, label='Total')

# Set x-axis label and tick labels
#plt.xlabel('Protocols')
plt.xticks([r + bar_width for r in range(len(user_key_gen_values))], labels)

# Set y-axis label
plt.ylabel('Gas cost consumption (gas)')

# Set title
plt.title('Gas cost complexity')

# Add legend
plt.legend()
plt.savefig('Gas cost complexity.png')

# Show the plot
plt.show()
