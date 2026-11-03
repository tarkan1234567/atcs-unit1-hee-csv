import csv


"""Meeting 3 - Linear Search Starter"""

def linear_search(data, target):
    """Return target index, or -1 when not present."""
    for index in range(len(data)):
        if data[index] == target:
            return index

    return -1


student_ids = []

with open('data/student_records_5000.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)  # Skip header row

    for row in reader:
        student_ids.append(row[0])


target_id = '781567'
result_index = linear_search(student_ids, target_id)

if result_index != -1:
    print(f"Target found at index {result_index}!")
else:
    print("Target not found.")