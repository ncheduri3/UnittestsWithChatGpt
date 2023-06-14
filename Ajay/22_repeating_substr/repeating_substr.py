def find_first_repeating_subsequence(string):
    n = len(string)

    # Check all possible subsequences of length 3
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                subsequence = string[i] + string[j] + string[k]

                # Check if the subsequence repeats
                if subsequence in string[k + 1:]:
                    return subsequence

    return ""
