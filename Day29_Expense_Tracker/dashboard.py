import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Expense Tracker", page_icon="💰")

st.title("💰 Smart Expense Tracker")
st.write("Analyze your monthly income, expenses and savings.")

file = st.file_uploader("Upload Expense CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expenses = df[df["Type"] == "Expense"]["Amount"].sum()
    savings = income - expenses

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"₹{income:,.0f}")
    col2.metric("Expenses", f"₹{expenses:,.0f}")
    col3.metric("Savings", f"₹{savings:,.0f}")

    expense_data = df[df["Type"] == "Expense"]

    category = expense_data.groupby("Category")["Amount"].sum()

    st.subheader("📊 Spending by Category")
    st.bar_chart(category)

    st.subheader("📋 Expense Data")
    st.dataframe(df)

    st.subheader("🔮 Expense Prediction")

    prediction = expenses

    st.success(
        f"Predicted next month expense: ₹{prediction:,.2f}"
    )

    report = pd.DataFrame({
        "Metric": ["Income", "Expenses", "Savings", "Predicted Expense"],
        "Amount": [income, expenses, savings, prediction]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        "⬇️ Download Report",
        csv,
        "expense_report.csv",
        "text/csv"
    )