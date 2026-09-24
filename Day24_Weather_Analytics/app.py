import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Weather Analytics",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Data Analytics Dashboard")

df = pd.read_csv("weather_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.sidebar.header("Filters")

cities = st.sidebar.multiselect(
    "Select Cities",
    df["City"].unique(),
    default=df["City"].unique()
)

filtered_df = df[df["City"].isin(cities)]

average_temp = filtered_df.groupby("City")["Temperature"].mean()

hottest_city = average_temp.idxmax()
coldest_city = average_temp.idxmin()

rainy_days = (filtered_df["Weather"] == "Rainy").sum()
sunny_days = (filtered_df["Weather"] == "Sunny").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡️ Average Temperature", 
            f"{filtered_df['Temperature'].mean():.1f} °C")

col2.metric("🔥 Hottest City", hottest_city)

col3.metric("🌧️ Rainy Days", rainy_days)

col4.metric("☀️ Sunny Days", sunny_days)

st.subheader("🌡️ Temperature Trend")

fig1, ax1 = plt.subplots()

for city in cities:
    city_data = filtered_df[filtered_df["City"] == city]
    ax1.plot(
        city_data["Date"],
        city_data["Temperature"],
        marker="o",
        label=city
    )

ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature")
ax1.legend()

st.pyplot(fig1)

st.subheader("📊 Average Temperature per City")

fig2, ax2 = plt.subplots()

average_temp.plot(kind="bar", ax=ax2)

ax2.set_xlabel("City")
ax2.set_ylabel("Average Temperature")

st.pyplot(fig2)

st.subheader("🌧️ Weather Distribution")

weather_counts = filtered_df["Weather"].value_counts()

fig3, ax3 = plt.subplots()

ax3.pie(
    weather_counts,
    labels=weather_counts.index,
    autopct="%1.1f%%"
)

ax3.set_title("Weather Distribution")

st.pyplot(fig3)

st.subheader("📋 Weather Data")

st.dataframe(filtered_df)

recent_temperatures = filtered_df["Temperature"].tail(3)

if len(recent_temperatures) > 0:
    prediction = recent_temperatures.mean()

    st.subheader("🔮 Tomorrow's Temperature")

    st.info(
        f"Predicted temperature: {prediction:.2f} °C"
    )

st.download_button(
    "⬇️ Download Report",
    filtered_df.to_csv(index=False),
    "weather_report.csv",
    "text/csv"
)