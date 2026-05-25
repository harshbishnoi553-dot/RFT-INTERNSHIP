import pandas as pd
import matplotlib.pyplot as plt

data = {
    "DATE": [
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08"
    ],
    "PRODUCT": [
        "Laptop","Mobile","Tablet","Laptop",
        "Mobile","Tablet","Laptop","Mobile"
    ],
    "REGION": [
        "North","South","East","West",
        "North","South","East","West"
    ],
    "SALES": [
        50000,30000,None,45000,
        35000,25000,55000,None
    ]
}

df = pd.DataFrame(data)

df["SALES"] = df["SALES"].fillna(df["SALES"].mean())

product_sales = df.groupby("PRODUCT")["SALES"].sum()

region_sales = df.groupby("REGION")["SALES"].sum()

df["DATE"] = pd.to_datetime(df["DATE"])

monthly_sales = df.groupby(df["DATE"].dt.month)["SALES"].sum()

best_region = region_sales.idxmax()

print("Total Sales Per Product")
print(product_sales)

print("\nRegion Wise Performance")
print(region_sales)

print("\nMonthly Growth Analysis")
print(monthly_sales)

print("\nBest Performing Region:", best_region)

plt.figure(figsize=(8,5))
plt.plot(df["DATE"], df["SALES"], marker='o')
plt.title("Sales Trends")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Top Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

print("\nKey Insights:")
print("1. Laptop has the highest sales.")
print("2. Missing values were handled using mean sales.")
print("3. North and East regions performed strongly.")
print("4. Sales trend shows overall growth.") 
print("5. Best performing region is", best_region)