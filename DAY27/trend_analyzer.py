import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

df = pd.read_csv("social_media_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

print("\n===== SOCIAL MEDIA TREND ANALYZER =====")

# Top Hashtags
hashtags = []

for tags in df["Hashtags"]:
    hashtags.extend(re.findall(r"#\w+", tags.lower()))

hashtag_count = Counter(hashtags)

top_hashtags = pd.DataFrame(
    hashtag_count.most_common(10),
    columns=["Hashtag", "Count"]
)

print("\nTop Hashtags:")
print(top_hashtags)

# Most Active Users
active_users = df["User"].value_counts().reset_index()
active_users.columns = ["User", "Posts"]

print("\nMost Active Users:")
print(active_users)

# Engagement Analysis
user_engagement = df.groupby("User")["Engagement"].sum().sort_values(ascending=False)

print("\nUser Engagement:")
print(user_engagement)

# Most Popular Posting Time
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

popular_time = df["Hour"].value_counts().idxmax()

print("\nMost Popular Posting Hour:", popular_time)

# Daily Engagement
daily_engagement = df.groupby("Date")["Engagement"].sum()

print("\nDaily Engagement:")
print(daily_engagement)

# Category Distribution
category_count = df["Category"].value_counts()

print("\nContent Category Distribution:")
print(category_count)

# Chart 1 - Top Hashtags
plt.figure(figsize=(8, 5))
plt.bar(top_hashtags["Hashtag"], top_hashtags["Count"])
plt.title("Top Trending Hashtags")
plt.xlabel("Hashtag")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_hashtags.png")
plt.show()

# Chart 2 - Daily Engagement
plt.figure(figsize=(8, 5))
plt.plot(daily_engagement.index, daily_engagement.values, marker="o")
plt.title("Daily Engagement Trend")
plt.xlabel("Date")
plt.ylabel("Engagement")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_engagement.png")
plt.show()

# Chart 3 - Category Distribution
plt.figure(figsize=(7, 7))
plt.pie(
    category_count.values,
    labels=category_count.index,
    autopct="%1.1f%%"
)
plt.title("Content Category Distribution")
plt.savefig("category_distribution.png")
plt.show()

# Export Report
report = df[
    [
        "Post_ID",
        "User",
        "Date",
        "Time",
        "Hashtags",
        "Likes",
        "Comments",
        "Shares",
        "Engagement",
        "Category"
    ]
]

report.to_csv("analytics_report.csv", index=False)

print("\nAnalytics report exported successfully!")
print("File: analytics_report.csv")