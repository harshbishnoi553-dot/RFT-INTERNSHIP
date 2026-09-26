import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

def categorize(description):
    description = description.lower()

    if any(x in description for x in ["rent", "electricity", "mobile"]):
        return "Bills"
    elif any(x in description for x in ["grocery", "groceries"]):
        return "Food"
    elif any(x in description for x in ["restaurant", "movie", "netflix"]):
        return "Entertainment"
    elif any(x in description for x in ["uber", "transport"]):
        return "Transport"
    elif "shopping" in description:
        return "Shopping"
    elif "salary" in description:
        return "Income"
    else:
        return "Other"

df["Category"] = df["Description"].apply(categorize)

income = df[df["Type"] == "Income"]["Amount"].sum()
expenses = df[df["Type"] == "Expense"]["Amount"].sum()
savings = income - expenses
savings_rate = (savings / income) * 100 if income > 0 else 0

print("\n===== SMART EXPENSE TRACKER =====")
print(f"Total Income   : ₹{income:,.2f}")
print(f"Total Expenses : ₹{expenses:,.2f}")
print(f"Total Savings  : ₹{savings:,.2f}")
print(f"Savings Rate   : {savings_rate:.2f}%")

category_expense = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()

print("\n===== CATEGORY-WISE EXPENSES =====")
print(category_expense)

predicted_expense = expenses

print("\n===== EXPENSE PREDICTION =====")
print(f"Predicted Next Month Expense: ₹{predicted_expense:,.2f}")

summary = pd.DataFrame({
    "Metric": [
        "Total Income",
        "Total Expenses",
        "Total Savings",
        "Savings Rate",
        "Predicted Next Month Expense"
    ],
    "Value": [
        income,
        expenses,
        savings,
        savings_rate,
        predicted_expense
    ]
})

summary.to_excel("final_report.xlsx", index=False)
df.to_csv("categorized_expenses.csv", index=False)

plt.figure(figsize=(8, 5))
category_expense.plot(kind="bar")
plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.tight_layout()
plt.savefig("spending_trends.png")
plt.show()

print("\nReports generated successfully!")
print("Created:")
print("- final_report.xlsx")
print("- categorized_expenses.csv")
print("- spending_trends.png")