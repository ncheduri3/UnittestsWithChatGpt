def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    
    # Generate all possible pairs (u, v) and their sums
    for u in nums1:
        for v in nums2:
            pairs.append((u + v, u, v))
    
    # Sort the pairs based on their sums
    pairs.sort(key=lambda x: x[0])
    
    # Extract the k smallest pairs
    result = [[u, v] for _, u, v in pairs[:k]]
    
    return result
