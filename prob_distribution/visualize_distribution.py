import matplotlib.pyplot as plt

def visualize_distribution(x, y, title, xlabel, ylabel):
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()