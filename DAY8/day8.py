import pandas as pd

data = {
    "NAME": ["A", "B", "C", "D"],
    "DEPT": ["IT", "HR", "IT", "HR"],
    "SALARY": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

avg_salary = df.groupby("DEPT")["SALARY"].mean()

highest_paid = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]

employee_count = df.groupby("DEPT")["NAME"].count()

sorted_departments = avg_salary.sort_values(ascending=False)

print("Average Salary Per Department:")
print(avg_salary)

print("\nHighest Paid Employee Per Department:")
print(highest_paid)

print("\nEmployee Count Per Department:")
print(employee_count)

print("\nDepartments Sorted By Average Salary:")
print(sorted_departments)