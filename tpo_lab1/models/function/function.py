import math


def cos_power_series(x: float, iterations: int = 33) -> float:
    ans = 0
    for i in range(iterations):
        ans += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return ans
