import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

data = {
    "Student": ["Aman", "Riya", "Kunal", "Priya", "Rohit", "Sneha", "Arjun", "Pooja", "Vikas", "Neha"],
    "Marks": [78, 85, 67, 90, 56, 72, 88, 95, 60, 80]
}

df = pd.DataFrame(data)

print(df)

mean_value = df["Marks"].mean()
median_value = df["Marks"].median()
mode_value = df["Marks"].mode()[0]
skewness_value = skew(df["Marks"])

print("\nMean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Skewness:", skewness_value)

plt.figure(figsize=(10,6))

sns.histplot(df["Marks"], bins=5, kde=True, color="blue")

plt.axvline(mean_value, color="red", linestyle="--", label=f"Mean = {mean_value:.2f}")
plt.axvline(median_value, color="green", linestyle="-.", label=f"Median = {median_value:.2f}")
plt.axvline(mode_value, color="orange", linestyle=":", label=f"Mode = {mode_value}")

plt.title("Distribution Analysis of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()

if skewness_value > 0:
    print("\nData is Positively Skewed")
elif skewness_value < 0:
    print("\nData is Negatively Skewed")
else:
    print("\nData is Symmetrical")