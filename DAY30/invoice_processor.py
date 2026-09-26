import pandas as pd

df = pd.read_csv("invoice_data.csv")

df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["due_date"] = pd.to_datetime(df["due_date"])

df["item_total"] = df["quantity"] * df["unit_price"]

df["total_amount"] = df.groupby("invoice_number")["item_total"].transform("sum")

today = pd.Timestamp.today().normalize()

df["status"] = df["due_date"].apply(
    lambda x: "Overdue" if x < today else "Pending"
)

df.to_csv("consolidated_invoice_report.csv", index=False)

print("\n===== INVOICE SUMMARY =====")
print("Total Invoices:", df["invoice_number"].nunique())
print("Total Amount: ₹", df.drop_duplicates("invoice_number")["total_amount"].sum())
print("Overdue Invoices:", df[df["status"] == "Overdue"]["invoice_number"].nunique())

print("\n===== OVERDUE INVOICES =====")

overdue = df[df["status"] == "Overdue"]

if overdue.empty:
    print("No overdue invoices")
else:
    print(
        overdue[
            ["invoice_number", "customer_name", "due_date", "total_amount"]
        ].drop_duplicates("invoice_number").to_string(index=False)
    )

print("\nReport created successfully!")