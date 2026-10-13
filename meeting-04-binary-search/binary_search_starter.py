import csv
from pathlib import Path

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


file_path = Path(__file__).resolve().parent.parent / "data" / "student_records_5000.csv"

numbers = []

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        numbers.append(int(row[0]))

numbers.sort()

target = 45
result = binary_search(numbers, target)

if result == -1:
    print(f"{target} was not found.")
else:
    print(f"{target} was found at index {result}.")