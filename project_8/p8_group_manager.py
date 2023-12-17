# CS 122 fall 2023 project 8
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: Create a group manager with dictionaries and lists

def cmd_help(d: dict):
    """
    The help function to this group manager

    Args:
        d: the main_dic

    Returns:
        None
    """
    commands = ["?", "C", "G", "A", "L", "X"]
    commands_description = ["list commands", "Create a new group", "List groups", "Add data to a group",
                            "List data for a group", "Exit"]
    for i in range(len(commands)):
        print(f"{commands[i]}: {commands_description[i]}")


def create_group(d: dict):
    """
    Creates a group without any data in the main_dict

    Args:
         d (dict): the main_dict that have all the groups

    Returns:
        None
    """
    print("** Create new group **\n")
    group = {'_fields_': [], '_data_': []}
    while group_name := input("Enter group name (empty to cancel): \n"):
        if group_name in d:
            print("This group name already exist")
        else:
            while field := input("Enter field name (empty to stop): \n"):
                if field in group['_fields_']:
                    print("This field name already exist")
                else:
                    group['_fields_'].append(field)
        print("")
        d.setdefault(group_name, group)
    print("")


def list_groups(d: dict):
    """
    Prints out all the groups with their properties

    Args:
         d (dict): the main_dict that have all the groups

    Returns:
        None
    """
    print("** List of groups **")
    for key in d:
        print(f"{key} : {len(d[key]['_fields_'])} properties ({', '.join(d[key]['_fields_'])})")
    print("")


def add_group_data(d: dict):
    """
    Adds data to a group

    Args:
        d (dict): the main_dict

    Returns:
        None
    """
    print("** Add data to group **")
    list_groups(d)
    while group_name := input("Enter group (empty to cancel): \n"):
        if group_name not in d:
            print("Group does not exist")
        else:
            data = {}
            for field in d[group_name]['_fields_']:
                data.setdefault(field, input(f"Enter {field}: \n"))
            d[group_name]['_data_'].append(data)
        print("")
    print("")


def list_group_data(d: dict):
    """
    Lists all the data in a group

    Args:
        d (dict): the main_dict

    Returns:
        None
    """
    print("** List group data **")
    list_groups(d)
    while group_name := input("Enter group name (empty to cancel): \n"):
        if group_name not in d:
            print("Group does not exist")
        else:
            data = d[group_name]['_data_']
            for i in data:  # i: dict
                print(f"{data.index(i)} {', '.join([f'{key} = {val}' for key, val in i.items()])}")
        print("")
    print("")


def start():
    """
    The main function

    Returns:
         None
    """
    print(">> Welcome to Group Manager <<")
    print("This program creates groups with dynamic properties")
    print("")

    commands = ["?", "C", "G", "A", "L", "X"]

    commands_functions = [cmd_help, create_group, list_groups, add_group_data, list_group_data]
    main_dict = {}
    while cmd := input("Command (empty or X to quit, ? for help): \n"):
        if cmd.upper() == "X":
            break
        elif cmd.upper() in commands:
            commands_functions[commands.index(cmd.upper())](main_dict)
        else:
            print("Not a valid function")


start()
