import random


class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self) -> str:
        return f"{self.year:4}. {self.month:02}. {self.day:02}."


def gen_dates(count):
    dates = []
    while len(dates) < count:
        year = random.randint(1900, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        dates.append(Date(year, month, day))
    return dates


def radix(dates):
    counts = [0] * 32
    for date in dates:
        counts[date.day] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    result = [None] * len(dates)
    for date in reversed(dates):
        counts[date.day] -= 1
        result[counts[date.day]] = date
    dates = result
    # dates, result = result, dates

    counts = [0] * 13
    for date in dates:
        counts[date.month] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    result = [None] * len(dates)
    for date in reversed(dates):
        counts[date.month] -= 1
        result[counts[date.month]] = date
    dates = result
    # dates, result = result, dates

    counts = [0] * 128
    for date in dates:
        counts[date.year - 1900] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    result = [None] * len(dates)
    for date in reversed(dates):
        counts[date.year - 1900] -= 1
        result[counts[date.year - 1900]] = date
    dates = result
    # dates, result = result, dates

    return result


unsorted = gen_dates(10)
for date in unsorted:
    print(date)
print()
sorted_dates = radix(unsorted)
for date in sorted_dates:
    print(date)

# TODO
# - implement Date.__lt__()
# - compare running time of radix() vs sorted()
# - compare running times with @dataclass(order=True)
# - compare running times with datetime.date
