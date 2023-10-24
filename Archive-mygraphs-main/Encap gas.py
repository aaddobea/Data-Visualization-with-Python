import matplotlib.pyplot as plt

def plot_data(data):
    schemes = data.keys()
    x = [20, 40, 60, 80, 100,120]
    for scheme in schemes:
        y = data[scheme]
        plt.plot(x, y, label=scheme, linewidth=2.0, marker='o')
    plt.xlabel('Number of Participants', fontsize=10)
    plt.ylabel('Encap GasCost (in gas)', fontsize=10)
    plt.title('Encap Gas cost vs Participants', fontsize=12, fontweight='bold')
    plt.grid(alpha=0.8)
    plt.legend(loc='best', fontsize=10)
    plt.tight_layout()
    plt.show()

# Example data
data = {'IC-CHS': [1826000, 3652000, 5478000, 7304000, 9130000, 10956000],
        'NP-IoT': [2063000, 4126000, 6189000, 8252000, 10315000, 12378000],
        'IH-IoT': [246000, 492000, 738000, 984000, 1230000,1476000],
        'Proposed': [612000, 1224000, 1836000, 2448000, 3060000, 3672000]}


plot_data(data)





