def selection_sort(data):
    values = data.copy()

    for i in range(len(values)):
        min_index = i

        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j

        values[i], values[min_index] = values[min_index], values[i]

    return values


def insertion_sort(data):
    values = data.copy()

    for i in range(1, len(values)):
        current = values[i]
        j = i - 1

        while j >= 0 and values[j] > current:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = current

    return values


test_cases = [
    [64, 25, 12, 22, 11, 5],
    [1, 2, 3, 4, 5, 7, 6],
    [7, 6, 5, 4, 3, 2, 1],
    [7, 7, 3, 7, 2, 1, 14],
    [],
    [42]
]

for data in test_cases:
    expected = sorted(data)

    selection_result = selection_sort(data)
    insertion_result = insertion_sort(data)

    print("Original:", data)
    print("Expected:", expected)
    print("Selection:", selection_result)
    print("Insertion:", insertion_result)
    print()
