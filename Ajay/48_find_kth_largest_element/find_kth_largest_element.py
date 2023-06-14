def find_kth_largest(nums, k):
    # Sort the array in descending order
    sorted_nums = sorted(nums, reverse=True)
    
    # Return the kth largest element
    return sorted_nums[k - 1]
