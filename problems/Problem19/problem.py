from datetime import datetime, timedelta


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def get_first_sunday_date_from(date: datetime) -> datetime:
    remaining_days_to_next_sunday = 6 - date.weekday()
    if remaining_days_to_next_sunday == 0:
        return date

    return date + timedelta(days=remaining_days_to_next_sunday)


def get_all_sundays_between_days(start: datetime, stop: datetime):
    if start > stop:
        raise ValueError('Start date cannot be greater than stop')

    sundays = []
    sunday = get_first_sunday_date_from(start)
    while sunday <= stop:
        sundays.append(sunday)
        sunday = sunday + timedelta(days=7)

    return sundays


def get_all_sundays_between_days_which_are_first_day_of_month(start: datetime, stop: datetime):
    sundays = get_all_sundays_between_days(start, stop)
    return [sunday for sunday in sundays if sunday.day == 1]
