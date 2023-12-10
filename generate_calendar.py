import calendar
from datetime import date, timedelta


def last_weekday_of_month(year, month):
    _, last_day = calendar.monthrange(year, month)
    last_day_of_month = date(year, month, last_day)

    while last_day_of_month.weekday() > calendar.FRIDAY:
        last_day_of_month -= timedelta(days=1)

    return last_day_of_month


def calculate_last_weekday_for_next_two_years():
    current_year = date.today().year
    start_year = current_year - 1

    for year in range(start_year, current_year + 2):
        for month in range(1, 13):
            yield last_weekday_of_month(year, month)


if __name__ == "__main__":
    for last_weekday in calculate_last_weekday_for_next_two_years():
        year = last_weekday.year
        month = last_weekday.month
        weekday_name = calendar.day_name[last_weekday.weekday()]
        print(f"Last weekday of {calendar.month_name[month]} {year}: "
              f"{last_weekday.strftime('%Y-%m-%d')} ({weekday_name})")
