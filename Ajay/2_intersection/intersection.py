from collections import Counter


def intersection(nums1, nums2):
    # Count the occurrences of each element in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    # Find the common elements
    common_elements = count1.keys() & count2.keys()

    # Create a list containing the common elements repeated the minimum number of times
    result = []
    for num in common_elements:
        count = min(count1[num], count2[num])
        result.extend([num] * count)

    return sorted(result)
