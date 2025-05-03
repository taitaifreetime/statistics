import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from typing import Tuple 
import argparse

from utility.poisson import poisson
from visualize_distribution import visualize_distribution

def poisson_distribution(x: int, lam: int = 1) -> Tuple[np.array, np.array]:
    """poisson distribution

    Args:
        x (int): the number of occurrences
        lam (int): the mean number of the events

    Returns:
        Tuple[np.array, np.array]: x axis and y axis
    """
    y = np.array([])
    for i in range(0,x,1):
        y = np.append(y, poisson(i, lam))
    return np.arange(x), y


def main(n, lam):
    x, y = poisson_distribution(n, lam)
    visualize_distribution(
        x, 
        y, 
        f"Poisson Distribution (x = {str(n)}, lambda = {str(lam)})", 
        f"", 
        f"Probability")

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--x', default=None) 
parser.add_argument('-l', '--lam', default=None) 
args = parser.parse_args()
x = args.x
lam = args.lam
if __name__ == "__main__":
    main(
        int(x), # x
        int(lam)) # lambda