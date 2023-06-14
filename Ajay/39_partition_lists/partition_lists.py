def partition_lists(nums, x):
    less_than_x = []
    equal_to_x = []
    greater_than_x = []

    for num in nums:
        if num < x:
            less_than_x.append(num)
        elif num == x:
            equal_to_x.append(num)
        else:
            greater_than_x.append(num)

    return less_than_x, equal_to_x, greater_than_x
