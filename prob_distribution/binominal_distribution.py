import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from typing import Tuple 
import argparse

from utility.binominal import binominal
from visualize_distribution import visualize_distribution

def binominal_distribution(n: int, p: float) -> Tuple[np.array, np.array]:
    """binominal distribution

    Args:
        n (int): the number of trials of Bernoulli
        p (float): probability

    Returns:
        Tuple[np.array, np.array]: x axis and y axis
    """
    the_num_of_success = np.array([])
    for i in range(n):
        the_num_of_success = np.append(the_num_of_success, binominal(i, n, p))
    x = np.arange(n)
    return x, the_num_of_success


def main(n, p):
    x, y = binominal_distribution(n, p)
    visualize_distribution(
        x, 
        y, 
        f"Binominal Distribution (n = {str(n)}, p = {str(p)})", 
        f"The number of success", 
        f"Probability")

parser = argparse.ArgumentParser()
parser.add_argument('--n', '-n', default=50) 
parser.add_argument('--probability', '-p', default=0.5) 
args = parser.parse_args()
n = args.n
probability = args.probability
if __name__ == "__main__":
    main(int(n), float(probability))