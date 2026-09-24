import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

average_temp = df.groupby("City")["Temperature"].mean().sort_values(ascending=False)

hottest_city = average_temp.idxmax()
coldest_city = average_temp.idxmin()

rainy_days = (df["Weather"] == "Rainy").sum()
sunny_days = (df["Weather"] == "Sunny").sum()

print("Average Temperature by City:")
print(average_temp)

print("\nHottest City:", hottest_city)
print("Coldest City:", coldest_city)
print("Rainy Days:", rainy_days)
print("Sunny Days:", sunny_days)

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

weather_counts = df["Weather"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(weather_counts, labels=weather_counts.index, autopct="%1.1f%%")
plt.title("Weather Distribution")
plt.show()

plt.figure(figsize=(8, 5))
average_temp.plot(kind="bar")
plt.title("Average Temperature per City")
plt.xlabel("City")
plt.ylabel("Average Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

report = pd.DataFrame({
    "City": average_temp.index,
    "Average Temperature": average_temp.values
})

report.to_csv("weather_report.csv", index=False)

print("\nReport exported successfully!")
recent_temperatures = df["Temperature"].tail(3)

tomorrow_temperature = recent_temperatures.mean()

print("\nPredicted Temperature for Tomorrow:", round(tomorrow_temperature, 2), "°C")