import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

st.set_page_config(
    page_title="Social Media Trend Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Social Media Trend Analyzer")
st.write("Analyze hashtags, users, engagement and sentiment.")

df = pd.read_csv("social_media_data.csv")

df["Engagement"] = (
    df["Likes"] +
    df["Comments"] +
    df["Shares"]
)

def sentiment(text):
    score = TextBlob(str(text)).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

df["Sentiment"] = df["Text"].apply(sentiment)

# Sidebar
st.sidebar.header("Filters")

categories = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

users = st.sidebar.multiselect(
    "Select User",
    df["User"].unique(),
    default=df["User"].unique()
)

filtered_df = df[
    (df["Category"].isin(categories)) &
    (df["User"].isin(users))
]

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Posts",
    len(filtered_df)
)

col2.metric(
    "Total Likes",
    filtered_df["Likes"].sum()
)

col3.metric(
    "Total Comments",
    filtered_df["Comments"].sum()
)

col4.metric(
    "Total Shares",
    filtered_df["Shares"].sum()
)

st.subheader("📈 Engagement Data")

st.dataframe(filtered_df)

st.subheader("📊 Engagement by User")

user_engagement = filtered_df.groupby("User")["Engagement"].sum()

st.bar_chart(user_engagement)

st.subheader("🥧 Content Categories")

category_data = filtered_df["Category"].value_counts()

fig, ax = plt.subplots()

ax.pie(
    category_data.values,
    labels=category_data.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)

st.subheader("😊 Sentiment Analysis")

sentiment_data = filtered_df["Sentiment"].value_counts()

st.bar_chart(sentiment_data)

st.subheader("🔥 Top Hashtags")

all_hashtags = []

for tags in filtered_df["Hashtags"]:
    all_hashtags.extend(str(tags).split())

hashtag_count = pd.Series(all_hashtags).value_counts().head(10)

st.bar_chart(hashtag_count)