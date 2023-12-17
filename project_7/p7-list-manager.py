# CS 122 fall 2023 project 7
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: a list manager with pre-defined commands
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


def cmd_help():
    """
    the help function which gives you a list of commands

    Returns:
        None
    """
    n = get_max_list_item_size(commands) + 5
    print("*** Available commands ***")
    for i in commands:
        print(f"{pad_right(i.title(), n)}{commands_description[commands.index(i)]}")
    print("Empty to exit")


def cmd_add(t: list):
    """
    an add function that will ask you for items to add to the list until an empty string given

    Args:
        t (list): my_list, the main list that we are managing

    Returns:
        None
    """
    while item := input("Enter information (empty to top): "):
        t.append(item)
        print(f"Added, item count = {len(t)}")


def cmd_delete(t: list):
    """
    a delete function which will delete a given item by their index in the list, if list empty or empty input, exit

    Args:
        t (list): my_list, the main list we are managing

    Returns:
        None
    """
    for i in range(len(t)):
        print(f"{pad_right(str(i), 2)}{pad_left(t[i], 2)}")
    while len(t) and (index := input("Enter a number to delete (empty to exit): ")):
        if index.strip().isdigit():
            index = int(index)
            t.remove(t[index])
        for i in range(len(t)):
            print(f"{pad_right(str(i), 2)}{pad_left(t[i], 2)}")
    if len(t) == 0:
        print("All items deleted")


def cmd_list(t: list):
    """
    a display function which shows you the number of items, and the items in our main list (my_list)

    Args:
        t (list): my_list the main list

    Returns:
        None
    """
    print(f"List contains {len(t)} item(s)")
    for i in t:
        print(i)


def cmd_clear(t: list):
    """
    a clear function which empty's the list

    Args:
        t (list): my_list, the main list

    Returns:
        None
    """
    print(f"{len(t)} item(s) removed, list empty")
    s = len(t)
    for i in range(s):
        del t[0]


def get_max_list_item_size(t: list):
    return max([len(i) for i in t])


my_list = []
commands = ["add", "delete", "list",  "clear"]
commands_description = ["Add to list", "Delete information", "List information", "Clear list"]
commands_objs = [cmd_add, cmd_delete, cmd_list, cmd_clear]
while a := input("Enter a command (? for help): "):
    if a in commands:
        commands_objs[commands.index(a)](my_list)
    elif a == "?":
        cmd_help()
    elif a == "del":
        cmd_delete(my_list)
    else:
        print("Command doesn't exist!")

print("Goodbye!")
