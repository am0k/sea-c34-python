def lucas(n):
    """
    Calculate the lucas value of a given position.
    """
    num1 = 2
    num2 = 1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        while n > 1:
            num1 += lucas(n - num1)
            num2 += lucas(n - num2)
            return num1 + num2

print lucas(2)
print lucas(4)