def calculate_sum_exceed_index(arr, x):
    # Initialize the sum and index
    total_sum = 0
    index = 0

    # Iterate over the elements in the list
    for i, num in enumerate(arr):
        # Add the current number to the total sum
        total_sum += num

        # Check if the sum exceeds the given integer x
        if total_sum > x:
            index = i
            break

    # Check if the sum never exceeds x
    if total_sum <= x:
        index = len(arr)

    return index
