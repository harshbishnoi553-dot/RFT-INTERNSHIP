import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Portfolio Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Market Portfolio Analyzer")

df = pd.read_csv("stocks.csv")

df["Investment"] = df["Buy_Price"] * df["Quantity"]
df["Current_Value"] = df["Current_Price"] * df["Quantity"]
df["Profit_Loss"] = df["Current_Value"] - df["Investment"]
df["Return_%"] = (df["Profit_Loss"] / df["Investment"]) * 100

latest = df.groupby("Stock").tail(1)

total_investment = latest["Investment"].sum()
total_value = latest["Current_Value"].sum()
profit = total_value - total_investment
portfolio_return = (profit / total_investment) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Investment", f"₹{total_investment:,.0f}")
col2.metric("Current Value", f"₹{total_value:,.0f}")
col3.metric("Profit/Loss", f"₹{profit:,.0f}")
col4.metric("Return", f"{portfolio_return:.2f}%")

st.subheader("📊 Stock Performance")

st.dataframe(
    latest[
        [
            "Stock",
            "Sector",
            "Investment",
            "Current_Value",
            "Profit_Loss",
            "Return_%"
        ]
    ]
)

st.subheader("🏢 Sector-wise Investment")

sector_data = latest.groupby("Sector")["Investment"].sum()

st.bar_chart(sector_data)

st.subheader("📈 Portfolio Growth")

df["Date"] = pd.to_datetime(df["Date"])

daily = df.groupby("Date")["Current_Value"].sum()

st.line_chart(daily)

st.subheader("📉 Daily Return Analysis")

daily_return = daily.pct_change() * 100

st.line_chart(daily_return)

st.subheader("🔮 Moving Average Prediction")

moving_average = daily.rolling(3).mean()

if daily.iloc[-1] > moving_average.iloc[-1]:
    st.success("Predicted Trend: UPWARD 📈")
else:
    st.warning("Predicted Trend: DOWNWARD 📉")

st.subheader("🏆 Performance")

best = latest.loc[latest["Return_%"].idxmax()]
worst = latest.loc[latest["Return_%"].idxmin()]

st.write(
    "Best Performing Stock:",
    best["Stock"],
    f"({best['Return_%']:.2f}%)"
)

st.write(
    "Worst Performing Stock:",
    worst["Stock"],
    f"({worst['Return_%']:.2f}%)"
)