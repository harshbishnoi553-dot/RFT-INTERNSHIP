import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [22, 45, 25, 35, 52, 23, 40, 60],
    "Spending": [2000, 8000, 1500, 5000, 12000, 1800, 7000, 15000],
    "Visits": [5, 15, 4, 10, 20, 3, 12, 25]
}

df = pd.DataFrame(data)

def segment(spending):
    if spending >= 10000:
        return "High"
    elif spending >= 5000:
        return "Medium"
    else:
        return "Low"

df["Category"] = df["Spending"].apply(segment)

print(df)

high_value = df[df["Category"] == "High"]
low_engagement = df[df["Visits"] < 5]

print("\nHigh Value Customers:")
print(high_value)

print("\nLow Engagement Customers:")
print(low_engagement)

plt.hist(df["Spending"], bins=5)
plt.xlabel("Spending")
plt.ylabel("Customers")
plt.title("Customer Spending Distribution")
plt.show()

category_count = df["Category"].value_counts()

plt.pie(category_count, labels=category_count.index, autopct="%1.1f%%")
plt.title("Customer Categories")
plt.show()

print("\nBusiness Strategies:")
print("High Customers -> Offer premium memberships and rewards")
print("Medium Customers -> Give discount offers to increase spending")
print("Low Customers -> Send promotional campaigns and engagement emails")