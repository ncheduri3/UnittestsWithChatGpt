import re


def compute_time_difference(time1, time2):
    pattern = r"(\d{2}):(\d{2}):(\d{2}) ([ap]m)"
    match1 = re.match(pattern, time1)
    match2 = re.match(pattern, time2)
    
    hours1 = int(match1.group(1))
    minutes1 = int(match1.group(2))
    seconds1 = int(match1.group(3))
    meridiem1 = match1.group(4)
    
    hours2 = int(match2.group(1))
    minutes2 = int(match2.group(2))
    seconds2 = int(match2.group(3))
    meridiem2 = match2.group(4)
    
    if meridiem1 == "pm" and hours1 != 12:
        hours1 += 12
    elif meridiem1 == "am" and hours1 == 12:
        hours1 = 0
    
    if meridiem2 == "pm" and hours2 != 12:
        hours2 += 12
    elif meridiem2 == "am" and hours2 == 12:
        hours2 = 0
    
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    
    if total_seconds1 <= total_seconds2:
        time_difference = total_seconds2 - total_seconds1
    else:
        time_difference = (24 * 3600) - (total_seconds1 - total_seconds2)
    
    hours = time_difference // 3600
    minutes = (time_difference % 3600) // 60
    seconds = time_difference % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
