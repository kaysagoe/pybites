def binary_search(sequence, target):
    low_index = 0
    high_index = len(sequence) - 1
    mid_index = (high_index + low_index) // 2

    while sequence[mid_index] != target and low_index < high_index:
        if target > sequence[mid_index]:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
        mid_index = (high_index + low_index) // 2

    if sequence[mid_index] == target:
        return mid_index
    else:
        return None
