# CS 122 fall 2023 project 6 & 5
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: our module to use to make the formatted output
def pad_string(string, length, padding=" ", direction='left'):
    """

    Args:
        string (str): the string to be padded
        length (int): the length of the string after padding.
        padding (str): the element to pad with
        direction ('left' | 'right'): the direction of padding

    Returns:
        string (str) the string after padding
    """
    if direction.lower() == 'right':
        string = string[::-1]
    while len(string) <= length:
        string = padding + string
    if direction.lower() == 'right':
        string = string[::-1]
    return string


def pad_left(string, length, padding=' '):
    """
    uses the pad_string() to pad to the left

    Args:
        string (str): the string to be padded
        length (int): length
        padding (str): padding

    Returns:
        a padded string
    """
    return pad_string(string, length, padding=padding)


def pad_right(string, length, padding=' '):
    """
    uses the pad_string() to pad to the right

    Args:
        string (str): the string to be padded
        length (int): length
        padding (str): padding

    Returns:
        a padded string
    """
    return pad_string(string, length, padding=padding, direction='right')
