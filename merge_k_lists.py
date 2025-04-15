def merge_k_lists(arrs):
    if not arrs:
        return []
    
    if len(arrs) == 1:
        return arrs[0]
    
    mid = len(arrs) // 2
    left = merge_k_lists(arrs[:mid])
    right = merge_k_lists(arrs[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

lists = [[1, 4, 5], [1, 3, 4], [2, 6], [1, 5, 8], [0, 7]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)