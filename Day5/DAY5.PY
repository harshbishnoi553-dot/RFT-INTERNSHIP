# BASIC CSV READER (WITHOUT PANDAS)
# Using os module + handling missing values + average marks

import os

# Step 1: Create file path
current_folder = os.path.dirname(os.path.abspath(__file__))

file_name = os.path.join(current_folder, "students.csv")

print(file_name)

# Step 2: Check if file exists
if not os.path.exists(file_name):
    print("CSV file not found!")
else:

    students = []
    total_marks = 0
    valid_marks_count = 0

    # Step 3: Open and read file
    with open(file_name, "r") as file:

        # Read all lines
        lines = file.readlines()

        # First line contains headers
        headers = lines[0].strip().split(",")

        # Read remaining lines
        for line in lines[1:]:

            # Remove extra spaces/newline
            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            # Split data using comma
            values = line.split(",")

            # Handle missing values
            while len(values) < len(headers):
                values.append("N/A")

            # Create dictionary
            student = {}

            for i in range(len(headers)):

                key = headers[i].upper()
                value = values[i]

                # Convert AGE and MARKS into integers if possible
                if key in ["AGE", "MARKS"]:

                    if value.strip() == "" or value == "N/A":
                        student[key] = "Missing"

                    else:
                        student[key] = int(value)

                        # Calculate average marks
                        if key == "MARKS":
                            total_marks += int(value)
                            valid_marks_count += 1

                else:
                    student[key] = value

            # Add dictionary to list
            students.append(student)

    # Step 4: Print final data
    print("Student Data:\n")
    print(students)

    # Step 5: Calculate average
    if valid_marks_count > 0:
        average = total_marks / valid_marks_count
        print("\nAverage Marks:", average)
    else:
        print("\nNo valid marks found.")

