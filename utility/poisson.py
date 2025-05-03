from math import exp
from .factorial import factorial

def poisson(x: int, lam: int = 1) -> float:
    """poisson

    Args:
        x (int): the number of occurrences
        lam (int, optional): the mean number of the events. Defaults to 1.

    Returns:
        float: probability
    """
    return exp(-lam)*lam**x/factorial(x)

def main():
    print(poisson(1, 5))

if __name__ == "__main__": 
    main()