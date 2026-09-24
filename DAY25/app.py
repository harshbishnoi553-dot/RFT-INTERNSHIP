import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fraud Detection System", layout="wide")

st.title("💳 Fraud Detection & Transaction Analysis")
st.write("Day 24 - Python Internship Project")

df = pd.read_csv("transactions.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Amount"] = pd.to_numeric(df["Amount"])

threshold = st.sidebar.number_input(
    "High Value Threshold",
    min_value=1000,
    value=10000,
    step=1000
)

frequent_limit = st.sidebar.number_input(
    "Frequent Transaction Limit",
    min_value=1,
    value=4,
    step=1
)

search = st.sidebar.text_input("Search Account")

category_filter = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    df["Category"].isin(category_filter)
]

if search:
    filtered_df = filtered_df[
        filtered_df["Account"].str.contains(search, case=False, na=False)
    ]

duplicates = df[df.duplicated("Transaction_ID", keep=False)]

high_value = df[df["Amount"] > threshold]

account_counts = df["Account"].value_counts()

frequent_accounts = account_counts[
    account_counts >= frequent_limit
].index

suspicious = df[
    (df["Transaction_ID"].isin(duplicates["Transaction_ID"])) |
    (df["Amount"] > threshold) |
    (df["Account"].isin(frequent_accounts))
].copy()

def calculate_risk(row):
    score = 0

    if row["Amount"] > threshold:
        score += 50

    if row["Transaction_ID"] in duplicates["Transaction_ID"].values:
        score += 30

    if row["Account"] in frequent_accounts:
        score += 20

    return min(score, 100)

df["Risk_Score"] = df.apply(calculate_risk, axis=1)

suspicious = df[
    (df["Risk_Score"] > 0)
].copy()

suspicious.to_csv(
    "suspicious_transactions.csv",
    index=False
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", len(df))
col2.metric("Duplicate Transactions", len(duplicates))
col3.metric("High Value Transactions", len(high_value))
col4.metric("Suspicious Transactions", len(suspicious))

st.subheader("📋 Transaction Data")

st.dataframe(filtered_df, use_container_width=True)

st.subheader("⚠️ Suspicious Transactions")

st.dataframe(
    suspicious.sort_values(
        "Risk_Score",
        ascending=False
    ),
    use_container_width=True
)

st.download_button(
    "⬇️ Download Suspicious Transactions",
    suspicious.to_csv(index=False),
    "suspicious_transactions.csv",
    "text/csv"
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Transaction Category Chart")

    category_count = df["Category"].value_counts()

    fig, ax = plt.subplots()

    category_count.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Transactions")
    ax.set_title("Transactions by Category")

    st.pyplot(fig)

with col2:
    st.subheader("📈 Daily Transaction Trend")

    daily = df.groupby("Date")["Amount"].sum()

    fig, ax = plt.subplots()

    daily.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Transaction Amount")
    ax.set_title("Daily Transaction Trend")

    st.pyplot(fig)

st.subheader("💰 Top 10 Highest Transactions")

top10 = df.sort_values(
    "Amount",
    ascending=False
).head(10)

fig, ax = plt.subplots()

ax.bar(
    top10["Transaction_ID"],
    top10["Amount"]
)

ax.set_xlabel("Transaction ID")
ax.set_ylabel("Amount")
ax.set_title("Top 10 Highest Transactions")

plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("🚨 Risk Score Analysis")

risk_data = df.sort_values(
    "Risk_Score",
    ascending=False
)

st.dataframe(
    risk_data[
        [
            "Transaction_ID",
            "Account",
            "Amount",
            "Category",
            "Risk_Score"
        ]
    ],
    use_container_width=True
)