import pandas as pd
from textblob import TextBlob

df = pd.read_csv("social_media_data.csv")

def get_sentiment(text):
    score = TextBlob(str(text)).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Text"].apply(get_sentiment)

print(df[["Text", "Sentiment"]])

sentiment_count = df["Sentiment"].value_counts()

print("\nSentiment Analysis:")
print(sentiment_count)

df.to_csv("sentiment_report.csv", index=False)