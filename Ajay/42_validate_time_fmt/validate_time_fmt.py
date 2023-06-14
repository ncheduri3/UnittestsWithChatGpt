import re


def validate_time_format(time_str):
    pattern = r"^(1[0-2]|[1-9]):[0-5][0-9] (am|pm)$"
    return re.match(pattern, time_str) is not None
