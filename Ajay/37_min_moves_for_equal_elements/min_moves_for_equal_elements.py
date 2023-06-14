def min_moves_for_equal_elements(nums):
    n = len(nums)
    if n <= 1:
        return 0

    # Find the median element
    median = sorted(nums)[n // 2]

    # Calculate the total number of moves needed
    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves
