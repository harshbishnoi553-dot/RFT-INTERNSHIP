import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

students = ["AMIT", "RIYA", "JOHN"]

maths = [85, 92, 78]
science = [88, 95, 80]
english = [82, 90, 75]

df = pd.DataFrame({
    "Students": students,
    "Maths": maths,
    "Science": science,
    "English": english
})

x = np.arange(len(students))
width = 0.25

plt.figure(figsize=(8,5))
plt.bar(x - width, maths, width, label="Maths")
plt.bar(x, science, width, label="Science")
plt.bar(x + width, english, width, label="English")

plt.xticks(x, students)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Dashboard")
plt.legend()
plt.show()

print(df)
print(df.describe())