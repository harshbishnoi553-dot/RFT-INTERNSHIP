import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Movie Name": [
        "Inception",
        "Avengers Endgame",
        "Interstellar",
        "Titanic",
        "Joker",
        "Avatar",
        "The Dark Knight",
        "Frozen",
        "Black Panther",
        "Dangal"
    ],
    "Rating": [8.8, 8.4, 8.6, 7.9, 8.5, 7.8, 9.0, 7.5, 7.3, 8.4],
    "Genre": [
        "Sci-Fi",
        "Action",
        "Sci-Fi",
        "Romance",
        "Drama",
        "Sci-Fi",
        "Action",
        "Animation",
        "Action",
        "Sports"
    ],
    "Revenue": [
        829,
        2798,
        701,
        2187,
        1074,
        2923,
        1005,
        1450,
        1347,
        311
    ]
}

df = pd.DataFrame(data)

print("Movie Dataset:\n")
print(df)

highest_rated = df.sort_values(by="Rating", ascending=False)
print("\nHighest Rated Movies:\n")
print(highest_rated[["Movie Name", "Rating"]])

genre_profit = df.groupby("Genre")["Revenue"].sum().sort_values(ascending=False)
print("\nMost Profitable Genres:\n")
print(genre_profit)

top_5 = df.sort_values(by="Revenue", ascending=False).head(5)
print("\nTop 5 Movies by Revenue:\n")
print(top_5[["Movie Name", "Revenue"]])

correlation = df["Rating"].corr(df["Revenue"])
print("\nCorrelation Between Rating and Revenue:", correlation)

plt.figure(figsize=(8,5))
sns.barplot(x="Genre", y="Revenue", data=df)
plt.title("Genre vs Revenue")
plt.xticks(rotation=30)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Rating"], bins=5, kde=True)
plt.title("Rating Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Rating", y="Revenue", data=df)
plt.title("Rating vs Revenue Correlation")
plt.show()