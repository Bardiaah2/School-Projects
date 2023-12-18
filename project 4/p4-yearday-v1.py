# CS 122 Fall 2023 Project 4
# Author: Bardia Ahmadi Dafchahi
# Credit:
# Description: The first version of the project that does not use any functions except the is_leap_year()

# code the is_leap_year function
def is_leap_year(year):
    """
    Checks if the given year argument is a leap year or not

    Args:
        year (int): the year to check for leap year

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


def start():
    """
    main function

    :return: None
    """
    # get an integer input for the year through the input function and passing it to a variable(year)
    year = int(input("Enter year: "))

    # validate year
    if not year:
        print("Year must be > 0")
        return None

    leap_year = is_leap_year(year)

    # get an integer input for the day of the year through the inout function and passing it to a variable(day)
    day = int(input("Enter day of year: "))

    # validate day
    if not (day in range(1, 365+1 + leap_year)):
        if day <= 0:
            print("Day of year must be > 0")
        else:
            print(f"Day must be <= {365 + leap_year}")
        return None

    # Initialize variables to hold the month and the days and loop through the months and the last days of them
    month = ""
    d = 0
    for i in range(13):
        if d < day:
            # Initialize a variable to hold the previous month's last day
            d1 = d
            if i == 0:
                d += 31
                month = 'January'
            elif i == 1:
                d += 28 + leap_year
                month = 'February'
            elif i == 2:
                d += 31
                month = 'March'
            elif i == 3:
                d += 30
                month = 'April'
            elif i == 4:
                d += 31
                month = 'May'
            elif i == 5:
                d += 30
                month = 'June'
            elif i == 6:
                d += 31
                month = 'July'
            elif i == 7:
                d += 31
                month = 'August'
            elif i == 8:
                d += 30
                month = 'September'
            elif i == 9:
                d += 31
                month = 'October'
            elif i == 10:
                d += 30
                month = 'November'
            elif i == 11:
                d += 31
                month = 'December'
        else:
            # Print the month, day of the month (day - first day of the month) and the year
            print(f"{month} {day - d1}, {year}")
            return None


start()
