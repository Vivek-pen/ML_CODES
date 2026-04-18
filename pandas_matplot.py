import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create data
data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [88, 90, 78, 88]
}

df = pd.DataFrame(data)

# Step 2: Display data
print("Student Data:\n", df)

# Step 3: Calculate average marks
avg = df["Marks"].mean()
print("Average Marks:", avg)

median = df["Marks"].median()
print("Median Marks:", median)

mode = df["Marks"].mode()
print("Mode:", mode)

# Step 4: Plot bar chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
