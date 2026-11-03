def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both lists and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append any remaining elements from the left or right list
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(data):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(data) <= 1:
        return data
        
    # Divide: Find the midpoint and split the list into two halves
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    # Recursive calls: Sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Merge: Combine the sorted halves
    return merge(sorted_left, sorted_right)

values = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(values))
