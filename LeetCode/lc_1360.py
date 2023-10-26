class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def days_in_month(year, month):
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if month == 2 and is_leap(year):
                return 29
            return days[month - 1]

        d1 = list(map(int, date1.split("-")))
        d2 = list(map(int, date2.split("-")))

        def days_from_1971(year, month, day):
            days = 0
            for y in range(1971, year):
                days += 366 if is_leap(y) else 365
            for m in range(1, month):
                days += days_in_month(year, m)
            days += day
            return days

        days1 = days_from_1971(d1[0], d1[1], d1[2])
        days2 = days_from_1971(d2[0], d2[1], d2[2])

        return abs(days1 - days2)

