from .combination import combination

def binominal(x: int, n: int, p: float) -> float:
    """binominal coefficient

    Args:
        x (int): the number of success
        n (int): the number of trials
        p (float): probability

    Returns:
        float: probability of the number of success
    """
    return combination(n,x)*p**x*(1-p)**(n-x)


def main():
    print(binominal(9, 20, 0.5))

if __name__ == "__main__": 
    main()