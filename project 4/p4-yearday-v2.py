# CS 122 Fall 2023 Project 4
# Author: Bardia Ahmadi Dafchahi
# Credit:
# Description: The last version of the project to determine the month and day


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


def valid_year(year):  # 1
    """
    Validates that the year is a valid year

    Args:
        year (int): the year to be validated

    Returns:
        False if the year is invalid and True if valid year
    """
    if not year:
        print("Year must be > 0")
        return False
    return True


# valid_year(0)
def valid_day_of_year(year, day_of_year):  # 2
    """
    Validates the day of the year based on the year (leap or not)

    Args:
        year (int): the year that the day is being validated
        day_of_year (int): validates that this day is in the range of the days of the year

    Returns:
         True if the day is a valid day in year and False if not
    """
    days_in_year = get_days_in_year(year)
    if not (day_of_year in range(1, days_in_year + 1)):
        if day_of_year <= 0:
            print("Day of year must be > 0")
        else:
            print(f"Day must be <= {days_in_year}")
        return False
    return True


# valid_day_of_year(2020,0)
# valid_day_of_year(2020,367)
# valid_day_of_year(2021,366)
def input_year():  # 3
    """
    Prompts the user for a year to be inputted

    Returns:
        year if the inputted year is valid and 0 if not
    """
    year = int(input("Enter year: "))
    if valid_year(year):
        return year
    return 0


def input_day_of_year(year):  # 4
    """
    Prompts the user for a day in the year

    Args:
        year (int): the year that was inputted and also to check for leap year

    Returns:
        day if the day is valid in that year and 0 if not
    """
    day = int(input("Enter day of year: "))
    if valid_year(year) and valid_day_of_year(year, day):
        return day
    return 0


def get_days_in_year(year):  # 5
    """
    Returns the number of the days in the given year

    Args:
        year (int): year

    Returns:
        number of the days in the year if the year is valid and 0 if not
    """
    if valid_year(year):
        return 365 + is_leap_year(year)
    return 0


# get_days_in_year(2020)
# get_days_in_year(2021)
def valid_month(month):  # 6
    """
    validates if the month is between 1 and 12

    Args:
        month (int): the month to be validated

    Returns:
        True if the month is valid and if not False
    """
    if not (month in range(1, 13)):
        if not month:
            print("Month must be > 0")
        else:
            print("Month must be <= 12")
        return False
    return True


# valid_month(13)
# valid_month(0)

def translate_month(month):  # 7
    """
    Turns the number of the month to string

    Args:
        month (int): the number of month

    Returns:
        the string name of the month if valid and an empty string if invalid
    """
    month_string = ""
    if valid_month(month):
        if month == 1:
            month_string = 'January'
        elif month == 2:
            month_string = 'February'
        elif month == 3:
            month_string = 'March'
        elif month == 4:
            month_string = 'April'
        elif month == 5:
            month_string = 'May'
        elif month == 6:
            month_string = 'June'
        elif month == 7:
            month_string = 'July'
        elif month == 8:
            month_string = 'August'
        elif month == 9:
            month_string = 'September'
        elif month == 10:
            month_string = 'October'
        elif month == 11:
            month_string = 'November'
        elif month == 12:
            month_string = 'December'
    return month_string


# translate_month(3)
def get_days_in_month(year, month):  # 8
    """
    Returns the number of days in the given month of a year

    Args:
        year (int): the year - to check if the year is a leap year
        month (int): the number of month

    Returns:
        the number of the days if a valid month and year and 0 if not
    """
    days = 0
    if valid_month(month) and valid_year(year):
        if month == 1:
            days = 31
        elif month == 2:
            days = 28 + is_leap_year(year)
        elif month == 3:
            days = 31
        elif month == 4:
            days = 30
        elif month == 5:
            days = 31
        elif month == 6:
            days = 30
        elif month == 7:
            days = 31
        elif month == 8:
            days = 31
        elif month == 9:
            days = 30
        elif month == 10:
            days = 31
        elif month == 11:
            days = 30
        elif month == 12:
            days = 31
    return days


# get_days_in_month(2020, 2)
def valid_day(year, month, day):  # 9
    """
    A final validation of the day, month and the year

    Args:
        year (int): year
        month (int): month
        day (int): day

    Returns:
        True if valid, False if not
    """
    if valid_year(year) and valid_month(month) and valid_day_of_year(year, day):
        return True
    return False


def get_date_string(month, day, year):  # 10
    """
    Returns a string of the output if valid

    Args:
        month (int): month
        day (int): day
        year (int): year

    Returns:
        string of the month day, year or empty if invalid
    """
    if valid_day(year, month, day):
        return f"{translate_month(month)} {day}, {year}"
    return ""


def start():
    """
    main function

    Args:
        -
    Returns:
        None
    """
    # get an integer input for the year through the input function and passing it to a variable(year)
    year = input_year()

    # validate year
    if not year:
        return None

    # get an integer input for the day of the year through the inout function and passing it to a variable(day)
    day = input_day_of_year(year)

    # validate day
    if not day:
        return None

    # Initialize variables to hold the month and the days and loop through the months and the last days of them
    d = 0
    for i in range(1, 13):
        if d < day:
            # Initialize a variable to hold the previous month's last day
            d1 = d
            d += get_days_in_month(year, i)
            month_num = i
    if valid_day(year, month_num, day):
        # Print the month, day of the month (day - first day of the month) and the year
        print(get_date_string(month_num, day - d1, year))
        return None


start()
