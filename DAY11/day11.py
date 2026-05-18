import matplotlib.pyplot as plt


days = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 360]


highest_sale = max(sales)
lowest_sale = min(sales)

highest_day = days[sales.index(highest_sale)]
lowest_day = days[sales.index(lowest_sale)]


plt.figure(figsize=(8, 5))


plt.plot(days, sales,
         marker='o',
         linestyle='-',
         linewidth=3)

for i in range(len(days)):
    plt.text(days[i], sales[i] + 5, str(sales[i]), ha='center')


plt.scatter(highest_day, highest_sale, s=150, label="Highest Sale")


plt.scatter(lowest_day, lowest_sale, s=150, label="Lowest Sale")

plt.title("Weekly Sales Trend", fontsize=16)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Sales", fontsize=12)


plt.grid(True)


plt.legend()


print("----- SALES TREND ANALYSIS -----")
print(f"Highest Sales: {highest_sale} on {highest_day}")
print(f"Lowest Sales: {lowest_sale} on {lowest_day}")

if sales[-1] > sales[0]:
    print("Overall Trend: Sales Increased During the Week")
else:
    print("Overall Trend: Sales Decreased During the Week")

plt.show()
