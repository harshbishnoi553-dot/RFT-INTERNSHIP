def analyze_scores(marks):
    # Basic calculations
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Count above average
    above_avg = sum(1 for m in marks if m > average)

    # Grade distribution
    grades = {"A": 0, "B": 0, "C": 0, "Fail": 0}

    for m in marks:
        if m >= 90:
            grades["A"] += 1
        elif m >= 75:
            grades["B"] += 1
        elif m >= 50:
            grades["C"] += 1
        else:
            grades["Fail"] += 1

    # Return results
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "above_average": above_avg,
        "grades": grades
    }


# 🔹 Example usage
marks = [78, 85, 90, 67, 85, 92, 78]
result = analyze_scores(marks)

print("Average:", result["average"])
print("Highest:", result["highest"])
print("Lowest:", result["lowest"])
print("Above Average:", result["above_average"])
print("Grade Distribution:", result["grades"])