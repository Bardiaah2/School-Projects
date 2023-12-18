# CS 122 fall 2023 lab 4
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: Print the months and their respective numbers and the leap years

import calendar


def get_full_month(month_num):
    """
    Returns the name of the month number
d
    Args:
        month_num (int): the number of the month that the name would be printed

    Returns:
        a string including the name of the month
    """
    month = ""
    if month_num == 1:
        month = "January"
    elif month_num == 2:
        month = "February"
    elif month_num == 3:
        month = "March"
    elif month_num == 4:
        month = "April"
    elif month_num == 5:
        month = "May"
    elif month_num == 6:
        month = "June"
    elif month_num == 7:
        month = "July"
    elif month_num == 8:
        month = "August"
    elif month_num == 9:
        month = "September"
    elif month_num == 10:
        month = "October"
    elif month_num == 11:
        month = "November"
    elif month_num == 12:
        month = "December"
    else:
        print(f"Must be an integer between 1 and 12 ({month_num} is invalid)")
    return month


def test_get_full_month():
    """
    Uses the get_full_month 14 times passing it numbers from 0 to 13

    Args:
        None

    Returns:
        None
    """
    for num in range(14):
        print(num, get_full_month(num))


test_get_full_month()


def is_leap_year(year):
    """
    Checks if the given year argument is a leap year or not

    Args:
        the year to check for leap year

    Returns:
        Boolean value; True if year is a leap year and False if the year is nor
    """
    is_leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            is_leap = True
        elif year % 400 == 0:
            is_leap = True
    return is_leap


def test_is_leap_year(start_year, end_year):
    for year in range(start_year, end_year + 1):
        is_leap = is_leap_year(year)
        if is_leap:
            print(year)


test_is_leap_year(1996, 2112)


def validate_is_leap_year(start_year, end_year):
    mismatches = 0
    for i in range(start_year, end_year + 1):
        real = calendar.isleap(i)
        to_check = is_leap_year(i)
        if real != to_check:
            print(i)
            mismatches += 1
    if mismatches:
        print(f"There was {mismatches} mismatches")
    else:
        print("No mismatches found")


validate_is_leap_year(1996, 2112)
