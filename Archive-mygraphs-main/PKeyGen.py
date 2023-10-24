import matplotlib.pyplot as plt

def plot_data(data):
    schemes = data.keys()
    x = [20, 40, 60, 80, 100,120]
    for scheme in schemes:
        y = data[scheme]
        plt.plot(x, y, label=scheme, linewidth=2.0, marker='o')
    plt.xlabel('Number of Participants', fontsize=10)
    plt.ylabel('PKeyGen GasCost (in gas)', fontsize=10)
    plt.title('Participant KeyGen Gas cost vs Participants', fontsize=12, fontweight='bold')
    plt.grid(alpha=0.8)
    plt.legend(loc='best', fontsize=10)
    plt.tight_layout()
    plt.show()

# Example data
data = {'IC-CHS': [732000, 1464000, 2196000, 2928000, 3660000, 4392000],
        'NP-IoT': [120000, 240000, 360000, 480000, 600000, 720000],
        'IH-IoT': [1580000, 3160000, 4740000, 6320000, 7900000, 9480000],
        'Proposed': [240000	,480000, 720000, 960000, 1200000, 1440000]}


plot_data(data)





