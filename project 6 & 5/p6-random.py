# CS 122 fall 2023 project 6 & 5
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: Reading from another file and counting the integers and comments and calculating the average of integers
from p6_shared import pad_left, pad_right
import os


def start():
    while True:
        comments = 0
        integers = 0
        total = 0

        filename = input("Enter filename (blank to exit): ").strip()
        if not filename:
            return None

        if not os.path.exists(filename):
            print(f"Invalid filename: {filename}")
        else:
            fin = open(f"{filename}")
            while True:
                line = fin.readline()
                if '#' in line:
                    comments += 1
                elif not line:
                    break
                else:
                    integers += 1
                    total += int(line.strip())
            fin.close()
            num_spacing = 10
            label_spacing = 10
            print(f"{pad_right('Count:', label_spacing)}{pad_left(str(integers), num_spacing)}")
            print(f"{pad_right('Comments:', label_spacing)}{pad_left(str(comments), num_spacing)}")
            print(f"{pad_right('Total:', label_spacing)}{pad_left(str(total), num_spacing)}")
            print(f"{pad_right('Average:', label_spacing)}{pad_left(str(round(total / integers, 2)), num_spacing)}")


start()
