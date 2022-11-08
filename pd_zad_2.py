
def what_number(num):
    numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
               14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    if num < 20 or num % 10 == 0:
        return f"{numbers[num]}"
    else:
        div_num = num // 10
        div_num *= 10
        num_mod = num % 10
        return f"{numbers[div_num]} {numbers[num_mod]}"


def what_hour(hour):
    return f"{what_number(hour)}"


def time_description(n_of_hours, n_of_mins):
    hr_correct = (n_of_hours <= 12 and n_of_hours > 0)
    min_correct = (n_of_mins < 60 and n_of_mins >= 0)
    if (hr_correct is False) or (min_correct is False):
        return 'Incorrect Input Data!'

    hour = what_hour(n_of_hours)
    if n_of_mins == 0:
        return f"{hour} o'clock"
    elif n_of_mins == 30:
        return f"half past {hour}"
    else:
        to_or_past = ''
        if n_of_mins < 30:
            if n_of_mins == 15:
                to_or_past = " past "
            else:
                to_or_past = ' minutes past '
        elif n_of_mins > 30:
            n_of_mins = 60 - n_of_mins
            if n_of_mins == 15:
                to_or_past = " to "
            else:
                to_or_past = ' minutes to '
            n_of_hours += 1
            if n_of_hours == 13:
                n_of_hours = 1
            hour = what_hour(n_of_hours)
        min = what_number(n_of_mins)
        return f"{min}{to_or_past}{hour}"


print(time_description(1, 20))
