# CS 122 fall 2023 lab 8
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description:
import random


def gen_random_integer_list(num, start_range=1, end_range=100, sort_list='N'):
    t = []
    if num <= 0:
        print('num must be > 0')
    elif not isinstance(num, int):
        print('num must be an integer')
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print('start_range and end_range must be integers')
    else:
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)

        if sort_list.upper() == 'Y':
            t.sort()

    return t


def get_high_score(t):
    if not isinstance(t, list):
        print('List argument expected')
        result = -1
    elif not t:
        result = 0
    else:
        t_copy = t[:]
        t_copy.sort()
        result = t_copy[len(t_copy) - 1]

    return result


def get_low_score(t):
    if not isinstance(t, list):
        print('List argument expected')
        result = -1
    elif not t:
        result = 0
    else:
        t_copy = t[:]
        t_copy.sort()
        result = t_copy[0]

    return result


def get_mean_score(t):
    if not isinstance(t, list):
        print('List argument expected')
        avg = -1
    elif not t:
        avg = 0
    else:
        total = sum(t)
        avg = total / len(t)

    return avg


def get_median_score(t):
    if not isinstance(t, list):
        print('List argument expected')
        avg = -1
    elif not t:
        avg = 0
    else:
        t_copy = t[:]
        t_copy.sort()
        size = len(t_copy)
        if size == 1:
            result = t_copy[0]
        elif size % 2 == 0:
            result = (t_copy[size // 2] + t_copy[size // 2 - 1]) / 2
        else:
            result = t_copy[size // 2]

    return result


def count_range(t, low_score, high_score):
    if not isinstance(t, list):
        print('List argument expected')
        count = -1
    elif not isinstance(high_score, int) or not isinstance(low_score, int):
        print('start and end must be integers')
        count = -1
    elif not t:
        count = 0
    elif low_score >= high_score:
        print('start must be < end')
        count = -1
    else:
        count = 0
        i = 0
        t_copy = t[:]
        t_copy.sort()
        while i in range(len(t_copy) // 2):
            if t_copy[i] not in range(low_score, high_score + 1):
                del t_copy[i]
            if t_copy[len(t_copy) - 1 - i] not in range(low_score, high_score + 1):
                del t_copy[len(t_copy) - 1 - i]
            if (t_copy[i] in range(low_score, high_score + 1) and
                    t_copy[len(t_copy) - 1 - i] in range(low_score, high_score + 1)):
                break
        count = len(t_copy)

    return count


def list_range(t: list):
    print(f"A - {count_range(t, 90, 100)}")
    print(f"B - {count_range(t, 80, 89)}")
    print(f"C - {count_range(t, 70, 79)}")
    print(f"D - {count_range(t, 60, 69)}")
    print(f"F - {count_range(t, 0, 59)}")

