"""A collection of functions used to evaluate the number length model."""


import numpy as np


from scipy.optimize import bisect


def ul(n, m):
    return m * (np.floor(np.log(n)) + 1)


def ulh(n, m):
    return m * (np.log10(n) + 1)


@np.vectorize
def minimal_N(m, upper=None):
    """Return the minimal value of N given m via bisection."""
    lower = m / np.log(10)
    if upper is None:
        upper = 10 * m

    try:
        N  = bisect(lambda n: ulh(n, m) - n, lower, upper)
        return N
    except ValueError as error:
        print(error)
        print(f"Upper limit of {upper} is insufficient.")
