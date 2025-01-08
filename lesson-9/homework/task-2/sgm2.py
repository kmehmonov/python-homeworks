import csv
import os

# File paths
file_name = r"lesson-9\homework\task-2\grades.csv"
output_file = r"lesson-9\homework\task-2\ave_gr_2.csv"

# Read data from CSV
with open(file_name, "r") as f:
    dict_reader = csv.DictReader(f, delimiter=",")
    grades_dict_list = list(dict_reader)

# Calculate average grades for each subject
unique = {}
for row in grades_dict_list:
    subject = row["Subject"]
    grade = float(row["Grade"])
    
    if subject not in unique:
        unique[subject] = [grade]
    else:
        unique[subject].append(grade)
subject_and_avarage = [{"Subject": subject, "Average": sum(grades) / len(grades)} for subject, grades in unique.items()]

# Write average grades to CSV
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Subject", "Average"])
    writer.writeheader()
    writer.writerows(subject_and_avarage)

