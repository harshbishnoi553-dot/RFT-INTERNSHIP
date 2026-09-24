import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_performance.csv")

df = df.drop_duplicates()
df = df.dropna()

dept_avg = df.groupby("Department")["Performance"].mean().sort_values(ascending=False)

top_10 = df.nlargest(10, "Performance")

low_attendance = df[df["Attendance"] < 75]

print("Department-wise Average Performance:")
print(dept_avg)

print("\nTop 10 Performers:")
print(top_10[["Employee_Name", "Department", "Performance", "Attendance"]])

print("\nEmployees with Attendance Below 75%:")
print(low_attendance[["Employee_Name", "Department", "Performance", "Attendance"]])

plt.figure(figsize=(10, 5))
dept_avg.plot(kind="bar")
plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Performance")
plt.tight_layout()
plt.savefig("performance_comparison.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df["Employee_Name"], df["Attendance"], marker="o")
plt.title("Employee Attendance Trend")
plt.xlabel("Employee")
plt.ylabel("Attendance (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("attendance_trend.png")
plt.show()

plt.figure(figsize=(8, 8))
df["Department"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Department Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("department_distribution.png")
plt.show()

report = df.copy()
report["Department_Average_Performance"] = report["Department"].map(dept_avg)
report["Attendance_Below_75"] = report["Attendance"] < 75                                       

report.to_csv("employee_performance_final_report.csv", index=False)

print("\nFinal report exported successfully!")