import statistics

data = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))

import math

print("Square root:", math.sqrt(16))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Pi value:", math.pi)
print("Log of 100:", math.log(100,10))


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

from scipy import constants as c
print(c.pi)
print(c.e)
