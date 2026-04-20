# PYTHON CAPSTONE PROJECT
# Student Performance and Activity Analyzer

import json
import csv

# FUNCTIONS

# Task 26
def read_students():
    with open("students.txt", "r") as file:
        return file.read().splitlines()

# Task 27
def read_marks():
    with open("marks.json", "r") as file:
        data = json.load(file)
        return data["students"]

# Task 28
def read_attendance():
    with open("attendance.csv", "r") as file:
        data = csv.DictReader(file)
        return list(data)

# Task 29
def average_marks(mark_list):
    return sum(mark_list) / len(mark_list)

# Task 30
def attendance_percentage(days_present, total_days):
    return (int(days_present) / int(total_days)) * 100

# Task 31
def topper(student_data):
    return max(student_data, key=lambda x: x["marks"])

# Task 32
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# MAIN PROGRAM

# Task 1
students_txt = read_students()
print("Task 1 - Student Names:")
print(students_txt)

# Task 2
print("\nTask 2 - Total Entries:")
print(len(students_txt))

# Task 3
unique_students = set(students_txt)
print("\nTask 3 - Unique Student Names:")
print(unique_students)

# Task 4
name_count = {}
for name in students_txt:
    name_count[name] = name_count.get(name, 0) + 1
print("\nTask 4 - Count of Each Student:")
print(name_count)

# Task 5
with open("unique_students.txt", "w") as file:
    for name in unique_students:
        file.write(name + "\n")
print("\nTask 5 - unique_students.txt created")

# JSON SECTION

# Task 6
marks_data = read_marks()

# Task 7
print("\nTask 7 - Names and Marks:")
for student in marks_data:
    print(student["name"], "-", student["marks"])

# Task 8
highest_student = max(marks_data, key=lambda x: x["marks"])
print("\nTask 8 - Highest Marks:")
print(highest_student["name"], highest_student["marks"])

# Task 9
lowest_student = min(marks_data, key=lambda x: x["marks"])
print("\nTask 9 - Lowest Marks:")
print(lowest_student["name"], lowest_student["marks"])

# Task 10
marks_list = []
for student in marks_data:
    marks_list.append(student["marks"])
avg = average_marks(marks_list)
print("\nTask 10 - Average Marks:")
print(round(avg, 2))

# Task 11
print("\nTask 11 - Python Course Students:")
for student in marks_data:
    if student["course"] == "Python":
        print(student["name"])

# Task 12
course_count = {}
for student in marks_data:
    course = student["course"]
    course_count[course] = course_count.get(course, 0) + 1
print("\nTask 12 - Students in Each Course:")
print(course_count)

# CSV SECTION

# Task 13
attendance_data = read_attendance()

# Task 14
print("\nTask 14 - Attendance Details:")
for row in attendance_data:
    print(row)

# Task 15
attendance_dict = {}
print("\nTask 15 - Attendance Percentage:")
for row in attendance_data:
    percent = attendance_percentage(
        row["days_present"],
        row["total_days"]
    )
    attendance_dict[row["name"]] = percent
    print(row["name"], "-", round(percent, 2), "%")

# Task 16
print("\nTask 16 - Students Below 80% Attendance:")
for name, percent in attendance_dict.items():
    if percent < 80:
        print(name)

# Task 17
best_attendance = max(attendance_dict, key=attendance_dict.get)
print("\nTask 17 - Best Attendance:")
print(best_attendance)

# DATA STRUCTURES

# Task 18
print("\nTask 18 - Marks Analysis")
print("Highest:", max(marks_list))
print("Lowest :", min(marks_list))
print("Sum    :", sum(marks_list))

# Task 19
courses_tuple = tuple(student["course"] for student in marks_data)
print("\nTask 19 - Tuple of Courses:")
print(courses_tuple)

# Task 20
courses_set = set(courses_tuple)
print("\nTask 20 - Unique Courses:")
print(courses_set)

# Task 21
marks_dict = {}
for student in marks_data:
    marks_dict[student["name"]] = student["marks"]
print("\nTask 21 - Name : Marks")
print(marks_dict)

# Task 22
print("\nTask 22 - Name : Attendance %")
print(attendance_dict)

# CONDITIONS AND LOOPS

# Task 23
print("\nTask 23 - Pass / Fail")
for name, mark in marks_dict.items():
    if mark >= 50:
        print(name, "- Pass")
    else:
        print(name, "- Fail")

# Task 24
print("\nTask 24 - Grades")
for name, mark in marks_dict.items():
    print(name, "-", grade(mark))

# Task 25
print("\nTask 25 - Marks > 80 and Attendance > 85")
for name in marks_dict:
    if marks_dict[name] > 80 and attendance_dict[name] > 85:
        print(name)

# FINAL COMBINED ANALYSIS

# Task 33
final_data = {}
for student in marks_data:
    name = student["name"]
    final_data[name] = {
        "marks": student["marks"],
        "attendance": attendance_dict[name],
        "course": student["course"]
    }
print("\nTask 33 - Combined Data Structure:")
print(final_data)

# Task 34
print("\nTask 34 - Final Student Report")
for name, details in final_data.items():
    print(
        name,
        "| Marks:", details["marks"],
        "| Attendance:", round(details["attendance"], 2),
        "| Course:", details["course"],
        "| Grade:", grade(details["marks"])
    )

# Task 35
eligible_students = []
for name, details in final_data.items():
    if details["marks"] >= 75 and details["attendance"] >= 80:
        eligible_students.append(name)
print("\nTask 35 - Eligible Students:")
print(", ".join(eligible_students))

# Task 36
need_improvement = []
for name, details in final_data.items():
    if details["marks"] < 75 or details["attendance"] < 80:
        need_improvement.append(name)
print("\nTask 36 - Students Needing Improvement:")
print(", ".join(need_improvement))

# OUTPUT FILES

# Task 37
with open("report.txt", "w") as file:
    file.write("Student Report\n\n")
    for name, details in final_data.items():
        line = (
            f"{name} - Marks: {details['marks']} "
            f"- Attendance: {round(details['attendance'], 2)}% "
            f"- Grade: {grade(details['marks'])}\n"
        )
        file.write(line)
print("\nTask 37 - report.txt created")

# Task 38
with open("eligible_students.txt", "w") as file:
    for student in eligible_students:
        file.write(student + "\n")
print("Task 38 - eligible_students.txt created")

# FINAL CHALLENGE

# Task 39
print("\nTask 39 - Final Summary")
print("Topper:", topper(marks_data)["name"])
print("Best Attendance:", best_attendance)
print("Average Marks:", round(avg, 2))
print("Eligible Students:", ", ".join(eligible_students))
print("Students Needing Improvement:",", ".join(need_improvement))

# Task 40
print("\nTask 40 - Program completed using clean modular code.")