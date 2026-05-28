import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2025-05-01",
        "2025-05-02",
        "2025-05-03",
        "2025-05-04",
        "2025-05-05",
        "2025-05-06",
        "2025-05-07",
        "2025-05-08",
        "2025-05-09",
        "2025-05-10"
    ],
    "Stock Price": [120, 125, 123, 130, 128, 135, 140, 138, 145, 150]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

df["Moving Average"] = df["Stock Price"].rolling(window=3).mean()

peak = df["Stock Price"].max()
drop = df["Stock Price"].min()

print("Stock Dataset:\n")
print(df)

print("\nHighest Stock Price:", peak)
print("Lowest Stock Price:", drop)

volatility = df["Stock Price"].std()
print("Volatility:", volatility)

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Stock Price"], marker='o', label="Stock Price")
plt.plot(df["Date"], df["Moving Average"], marker='s', label="Moving Average")
plt.title("Stock Price Trend Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()