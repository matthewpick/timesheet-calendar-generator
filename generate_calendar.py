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

    for year in range(current_year, current_year + 2):
        for month in range(1, 13):
            last_weekday = last_weekday_of_month(year, month)
            weekday_name = calendar.day_name[last_weekday.weekday()]
            # print(f"Last weekday of {calendar.month_name[month]} {year}: {last_weekday.strftime('%Y-%m-%d')} ({weekday_name})")
            yield last_weekday

if __name__ == "__main__":
    calculate_last_weekday_for_next_two_years()
