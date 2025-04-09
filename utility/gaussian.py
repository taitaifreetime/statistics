from math import pi, exp

def gaussian(x: float, mean: float = 0.0, variance: float = 1.0) -> float:
    """

    Args:
        x (float): _description_
        mean (float, optional): _description_. Defaults to 0.0.
        variance (float, optional): _description_. Defaults to 1.0.

    Returns:
        float: gaussian
    """
    return (2*pi*variance)**(-1/2) * exp(-(x-mean)**2/(2*variance))


def main():
    print(gaussian(1.0))

if __name__ == "__main__": 
    main()