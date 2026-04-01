import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name":["a","b","c"],
    "marks": [11,22,33]
}

df = pd.DataFrame(data)

print("Student Data: ",df)

avg = df["marks"].mean();
print("Average marks: ",avg)

mode = df["marks"].mode()
print("Mode: ",mode)

plt.bar(df["name"],df["marks"])
plt.title("Student Data")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()