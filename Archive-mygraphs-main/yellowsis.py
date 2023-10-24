import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [[100, 125.0000908], [200, 384.6154659], [300, 546.1538335], [400, 687.5000702], [500, 748.076991], [600, 851.923141], [700, 944.2307419], [800, 1166.346162], [900, 1290.384575], [1000, 1437.499955]]

df = pd.DataFrame(data, columns=['Number of patients', 'Latency'])

sns.set(style="whitegrid")
sns.barplot(x='Number of patients', y='Latency', data=df, palette="husl")

plt.xlabel("Number of patients")
plt.ylabel("Latency")

plt.show()
