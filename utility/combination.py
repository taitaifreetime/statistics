from .factorial import factorial

def combination(n: int, x: int) -> int:
    """

    Args:
        n (int): the number of trials
        x (int): the number of choosing

    Returns:
        int: combination
    """
    return factorial(n)/(factorial(n-x)*factorial(x))


def main():
    print(combination(9, 3))

if __name__ == "__main__":
    main()