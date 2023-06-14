def increasing_triplet(nums):
    min_value = float('inf')
    second_min_value = float('inf')
    
    for num in nums:
        if num <= min_value:
            min_value = num
        elif num <= second_min_value:
            second_min_value = num
        else:
            return True

    return False
