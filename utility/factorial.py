def factorial(x: int) -> int:
    """

    Args:
        x (int): _description_

    Returns:
        int: factorial value
    """
    if 1 < x:
        return x * factorial(x-1) 
    elif 0 > x:
        return 0
    else:
        return 1


def main():
    print(factorial(4))

if __name__ == "__main__":
    main()