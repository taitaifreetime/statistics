import sys
import os 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from normal_distribution import normal_distribution
from visualize_distribution import visualize_distribution

def animate_normal_distribution():
    """animate normal distribution
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mean', default=None) 
    parser.add_argument('-v', '--variance', default=None) 
    args = parser.parse_args()
    mean = args.mean
    variance = args.variance

    n = 50
    x = np.arange(n) - n/2.0

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability")

    def init():
        line.set_data([], [])
        return line,

    def update_mean(frame):
        mean = -n/2 +  frame * 1.0

        _, y = normal_distribution(n, mean, variance)
        line.set_data(x, y)
        ax.set_title(f"Normal Distribution (mean={mean:.2f}, variance={variance:.2f})")  
        return line
    
    def update_variance(frame):
        if frame <= 10: variance = 1.0 + frame * 1.0 
        if frame > 10: variance = 1.0 + frame * 1.5
        elif variance > 20.0: variance = 1.0 + frame * 5.0 

        _, y = normal_distribution(n, mean, variance)
        line.set_data(x, y)
        ax.set_title(f"Normal Distribution (mean={mean:.2f}, variance={variance:.2f})")  
        return line
    
    if mean is None and variance is None:
        mean = 0.0
        variance = 1.0
        x, y = normal_distribution(n, mean, variance)
        line.set_data(x, y)
        ax.set_title(f"Normal Distribution (mean={mean:.2f}, variance={variance:.2f})")
        plt.tight_layout()
        plt.show()
    elif mean is not None and variance is not None:
        mean = float(mean)
        variance = float(variance)
        x, y = normal_distribution(n, mean, variance)
        line.set_data(x, y)
        ax.set_title(f"Normal Distribution (mean={mean:.2f}, variance={variance:.2f})")
        plt.tight_layout()
        plt.show()
    else:
        if mean is None:
            mean = 0.0
            variance = float(variance)
            ax.set_title(f"Normal Distribution (mean=??, variance={variance:.2f})")
            ani = FuncAnimation(fig, update_mean, frames=n, init_func=init, blit=False, interval=200)
        elif variance is None:
            variance = 1.0
            mean = float(mean)
            ax.set_title(f"Normal Distribution (mean={mean:.2f}, variance=??)")
            ani = FuncAnimation(fig, update_variance, frames=n, init_func=init, blit=False, interval=200)
        
        # ani.save('normal_distribution.gif', writer='imagemagick', fps=10)
        plt.tight_layout()
        plt.show()

def main():
    animate_normal_distribution()

if __name__ == "__main__":
    main()