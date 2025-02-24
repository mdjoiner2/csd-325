import json

# Function to print student list
def print_students(students, message):
    print(f"\n{message}\n" + "-" * 50)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print("-" * 50)

# Load the JSON file into a Python list
with open("student.json", "r") as file:
    students = json.load(file)

# Print original student list
print_students(students, "Original Student List")

# Add a new student
new_student = {
    "F_Name": "John",
    "L_Name": "Doe",
    "Student_ID": 99999,
    "Email": "jdoe@gmail.com"
}
students.append(new_student)

# Print updated student list
print_students(students, "Updated Student List")

# Write updated data back to the JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe .json file has been updated successfully.")
