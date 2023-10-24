import matplotlib.pyplot as plt
import numpy as np

def plot_data(data):
    schemes = data.keys()
    x = [20, 40, 60, 80, 100,120]
    for scheme in schemes:
        y = data[scheme]
        plt.plot(x, y, label=scheme, linewidth=2.0, marker='v')
    plt.xlabel('Number of Participants', fontsize=10)
    plt.ylabel('Decap GasCost (in gas)', fontsize=10)
    plt.title('Decap Gas cost vs Participants', fontsize=12, fontweight='bold')
    plt.grid(alpha=0.8)
    plt.legend(loc='best', fontsize=10)
    plt.tight_layout()
    plt.show()

# Example data
data = {
    'IC-CHS': [1480000, 2800000, 4040000, 5520000, 6900000, 8480000],
    'NP-IoT': [1823000,	3646000,5469000, 7292000, 9115000, 10938000],
    'IH-IoT': [1586000, 3172000, 4758000,6344000, 7930000,9516000],
    'Proposed': [252000, 504000, 756000, 1008000, 1260000, 1512000]
}



plot_data(data)




