import math


def sum_circle_areas(n):
    total_area = 0

    for radius in range(1, n+1):
        area = math.pi * radius ** 2
        total_area += area

    return total_area
