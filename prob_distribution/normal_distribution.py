import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from typing import Tuple 
import argparse

from utility.gaussian import gaussian
from visualize_distribution import visualize_distribution

def normal_distribution(n: int, mean: float, variance: float) -> Tuple[np.array, np.array]:
    """normal distribution

    Args:
        n (int): 
        mean (float): 
        variance (float): 

    Returns:
        Tuple[np.array, np.array]: x axis and y axis
    """
    y = np.array([])
    for i in range(n):
        y = np.append(y, gaussian(float(i) - n/2.0, mean, variance))
    x = np.arange(n) - n/2.0
    return x, y


def main(mean, variance):
    n = 50
    x, y = normal_distribution(n, mean, variance)
    visualize_distribution(
        x, 
        y, 
        f"Normal Distribution (mean = {str(mean)}, variance = {str(variance)})", 
        f"", 
        f"Probability")

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mean', default=None) 
parser.add_argument('-v', '--variance', default=None) 
args = parser.parse_args()
mean = args.mean
variance = args.variance
if __name__ == "__main__":
    main(
        float(mean), # mean 
        float(variance)) # variance