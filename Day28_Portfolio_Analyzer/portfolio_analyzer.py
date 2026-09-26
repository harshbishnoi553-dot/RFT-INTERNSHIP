import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stocks.csv")

df["Investment"] = df["Buy_Price"] * df["Quantity"]
df["Current_Value"] = df["Current_Price"] * df["Quantity"]
df["Profit_Loss"] = df["Current_Value"] - df["Investment"]
df["Return_%"] = (df["Profit_Loss"] / df["Investment"]) * 100

latest = df.groupby("Stock").tail(1)

print("\n===== STOCK PORTFOLIO ANALYZER =====\n")

print("Stock Performance:")
print(latest[["Stock", "Sector", "Investment", "Current_Value", "Profit_Loss", "Return_%"]])

best = latest.loc[latest["Return_%"].idxmax()]
worst = latest.loc[latest["Return_%"].idxmin()]

print("\nBest Performing Stock:")
print(best["Stock"], "-", round(best["Return_%"], 2), "%")

print("\nWorst Performing Stock:")
print(worst["Stock"], "-", round(worst["Return_%"], 2), "%")

total_investment = latest["Investment"].sum()
total_value = latest["Current_Value"].sum()
total_profit = total_value - total_investment
overall_return = (total_profit / total_investment) * 100

print("\nPortfolio Summary:")
print("Total Investment:", total_investment)
print("Current Value:", total_value)
print("Total Profit/Loss:", total_profit)
print("Overall Return:", round(overall_return, 2), "%")

sector_data = latest.groupby("Sector")["Investment"].sum()

plt.figure(figsize=(8, 5))
sector_data.plot(kind="bar")
plt.title("Sector-wise Investment")
plt.xlabel("Sector")
plt.ylabel("Investment")
plt.tight_layout()
plt.savefig("sector_investment.png")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])

daily = df.groupby("Date")["Current_Value"].sum().reset_index()
daily["Daily_Return_%"] = daily["Current_Value"].pct_change() * 100

plt.figure(figsize=(8, 5))
plt.plot(daily["Date"], daily["Current_Value"], marker="o")
plt.title("Portfolio Growth")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("portfolio_growth.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(daily["Date"], daily["Daily_Return_%"], marker="o")
plt.title("Daily Return Analysis")
plt.xlabel("Date")
plt.ylabel("Daily Return %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_returns.png")
plt.show()

daily["Moving_Average"] = daily["Current_Value"].rolling(3).mean()

if daily["Current_Value"].iloc[-1] > daily["Moving_Average"].iloc[-1]:
    trend = "UPWARD"
else:
    trend = "DOWNWARD"

print("\nNext Day Trend Prediction:", trend)

print("\nCharts generated successfully!")