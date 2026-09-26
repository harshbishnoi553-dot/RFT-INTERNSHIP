import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Invoice Processing System",
    page_icon="🧾"
)

st.title("🧾 Automated Invoice Processing System")

file = st.file_uploader("Upload Invoice CSV", type=["csv"])

if file:

    df = pd.read_csv(file)

    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["due_date"] = pd.to_datetime(df["due_date"])

    df["item_total"] = df["quantity"] * df["unit_price"]

    df["total_amount"] = df.groupby(
        "invoice_number"
    )["item_total"].transform("sum")

    today = pd.Timestamp.today().normalize()

    df["status"] = df["due_date"].apply(
        lambda x: "Overdue" if x < today else "Pending"
    )

    unique = df.drop_duplicates("invoice_number")

    total_invoices = len(unique)
    total_amount = unique["total_amount"].sum()
    overdue = len(unique[unique["status"] == "Overdue"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Invoices", total_invoices)
    col2.metric("Total Amount", f"₹{total_amount:,.2f}")
    col3.metric("Overdue", overdue)

    st.subheader("Invoice Report")

    st.dataframe(df, use_container_width=True)

    st.subheader("Overdue Invoices")

    overdue_df = unique[unique["status"] == "Overdue"]

    st.dataframe(
        overdue_df[
            ["invoice_number", "customer_name", "due_date", "total_amount"]
        ],
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Report",
        csv,
        "consolidated_invoice_report.csv",
        "text/csv"
    )

else:
    st.info("Upload invoice_data.csv to start.")