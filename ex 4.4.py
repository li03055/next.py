def gen_secs():
    sec_generator = (n for n in range(0, 60))
    return sec_generator

def gen_minutes():
    min_generator = (n for n in range(0, 60))
    return min_generator

def gen_hours():
    hour_generator = (n for n in range(0, 24))
    return hour_generator

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)

# for gt in gen_time():
#     print(gt)

def gen_years(start = 2023):
    while True:
        yield start
        start = start + 1

def gen_months():
    month_generator = (n for n in range(1, 13))
    return month_generator

def gen_days(month, leap_year=True):
    if month == 2:
        if leap_year:
            yield 29
        else:
            yield 28
    elif month in [4, 6, 9, 11]:
        yield 30
    else:
        yield 31

def check_leap_year(year):  # check if year is leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, leap_year=check_leap_year(year)):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"


date_generator = gen_date()

for i, date in enumerate(date_generator, start=1):
    if i % 1000000 == 0:
        print(date)






