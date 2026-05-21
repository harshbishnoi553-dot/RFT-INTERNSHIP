import matplotlib.pyplot as plt

categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

plt.figure(figsize=(6,6))
plt.pie(
    expenses,
    labels=[f"{c} {e/sum(expenses)*100:.1f}%" for c, e in zip(categories, expenses)],
    autopct='%1.1f%%'
)

highest = categories[expenses.index(max(expenses))]
print("Highest Category:", highest)

plt.title("Category Breakdown")
plt.show()