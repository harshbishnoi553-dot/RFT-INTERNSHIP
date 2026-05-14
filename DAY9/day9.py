employees = [
    {"name": "Harsh", "age": 21, "salary": 90000},
    {"name": "Aman", "age": 32, "salary": 45000},
    {"name": "Riya", "age": 28, "salary": 75000},
    {"name": "Karan", "age": 22, "salary": 52000},
    {"name": "Neha", "age": 35, "salary": 80000}
]

filtered_data = [
    employee
    for employee in employees
    if employee["salary"] > 50000 and employee["age"] < 30
]

print("Filtered Results:\n")

for employee in filtered_data:
    print(employee)

with open("filtered_data.txt", "w") as file:
    for employee in filtered_data:
        file.write(str(employee) + "\n")

print("\nFiltered data saved successfully.")
