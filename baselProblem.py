from resultPrinter import printer
from math import sqrt

# The precise summation of the reciprocals of the squares of the natural numbers is (PI**2)/6
def baselProblemMethod(n=10):
    # Initial pi value
    pi_value = 0

    # For every number from 1 to n, add 1/(i**2) to pi value
    for i in range(1, n+1):
        pi_value += 1/(i**2)

    # For get pi value: sqrt(summation * 6)
    pi_value = sqrt(pi_value * 6)
    printer(pi_value)

baselProblemMethod(100000)
