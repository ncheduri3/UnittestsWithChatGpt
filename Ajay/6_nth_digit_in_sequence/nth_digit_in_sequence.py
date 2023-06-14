def nth_digit_in_sequence(n):
    if n == 0:
        return None

    digit_count = 1
    start_num = 1
    end_num = 9

    while n > digit_count * (end_num - start_num + 1):
        n -= digit_count * (end_num - start_num + 1)
        digit_count += 1
        start_num *= 10
        end_num = end_num * 10 + 9

    num = start_num + (n - 1) // digit_count
    digit_position = (n - 1) % digit_count

    return int(str(num)[digit_position])
