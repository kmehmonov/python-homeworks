import csv
import os


file_name = r"lesson-9\homework\task-2\grades.csv"
output_file = r"lesson-9\homework\task-2\ave_gr_1.csv"

# Read data from CSV
with open(file_name, "r") as f:
    list_reader = csv.reader(f, delimiter=",")
    headers = next(list_reader)
    grades_list = list(list_reader)


# Calculate average grades for each subject
subject_and_average = []
unique_subjects = {subject for _, subject, _ in grades_list}

for subject in unique_subjects:
    average = sum(int(grade) for _, sub, grade in grades_list if sub == subject) / len([grade for _, sub, grade in grades_list if sub == subject])
    subject_and_average.append([subject, average])

# Write average grades to CSV
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Average"])
    writer.writerows(subject_and_average)