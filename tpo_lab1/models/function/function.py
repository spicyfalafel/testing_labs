import math


def sin_power_series(x: float, iterations: int = 42) -> float:
    ans = 0
    for i in range(1, iterations):
        ans += ((-1) ** (i-1)) * (x ** (2 * i - 1)) / math.factorial(2 * i - 1)
    return ans
