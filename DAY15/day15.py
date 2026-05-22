import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 170, 160, 180, 200],
    "Profit": [20, 25, 30, 28, 35, 40]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit Comparison")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

print(df.describe())

