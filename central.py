import statistics as s

data = list(map(float, input("Enter data: ").split()))

print("Statistical Methods")
print("Central Tendency Measures:")

print("Mean is :", s.mean(data))
print("Median is :", s.median(data))
print("Mode is :", s.mode(data))

print("Measures of dispersion")

print("Variance is :", s.variance(data))
print("Standard Deviation is :", s.stdev(data))
