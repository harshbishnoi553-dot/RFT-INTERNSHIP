import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\harsh\RFT INTERNSHIP\DAY20\dataset.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df.describe())

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(col)
    plt.show()

if len(numeric_cols) > 1:
    plt.figure(figsize=(10,6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
    plt.show()

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

if len(numeric_cols) >= 2:
    sns.pairplot(df[numeric_cols])
    plt.show()

insights = {}

for col in numeric_cols:
    insights[col] = {
        "mean": df[col].mean(),
        "median": df[col].median(),
        "max": df[col].max(),
        "min": df[col].min()
    }

print(insights)

df.to_csv("cleaned_dataset.csv", index=False)