import matplotlib.pyplot as plt

def plot_data(data):
    schemes = data.keys()
    x = [20, 40, 60, 80, 100, 120]
    for scheme in schemes:
        y = data[scheme]
        plt.plot(x, y, label=scheme, linewidth=2.0, marker='o')
    plt.xlabel('Number of Participants', fontsize=10)
    plt.ylabel('Total GasCost (in gas)', fontsize=10)
    plt.title('Total Gas cost vs Participants', fontsize=12, fontweight='bold')
    plt.grid(alpha=0.8)
    plt.legend(loc='best', fontsize=10)
    plt.tight_layout()
    plt.show()

# Example data
data = {'IC-CHS': [4138000,8276000,12414000,16552000,20690000,24828000],
        'NP-IoT': [4006000,8012000,12018000, 16024000, 20030000, 24036000],
        'IH-IoT': [3412000, 6824000, 10236000,13648000,17060000,20472000],
        'Proposed': [1104000, 2208000, 3312000, 4416000, 5520000, 6624000]}



plot_data(data)





