# CS 122 fall 2023 lab 10
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description:
import os


def number_stats(*args):
    count = len(args)
    minimum = min(args)
    maximum = max(args)
    sorted_args = sorted(args)
    if count % 2 == 1:
        median = (sorted_args[count // 2 - 1] + sorted_args[count // 2]) / 2
    else:
        median = sorted_args[count // 2]
    mean = sum(args) / count
    return count, minimum, maximum, mean, median


def get_file():
    data = []
    if os.path.exists(file := input("Enter file name: ")):
        fin = open(file)
        fin.readline()
        for line in fin:
            line = line.strip()
            data.append(int(line))
        fin.close()
    return tuple(data)


__length, __min, __max, __mean, __median = number_stats(*get_file())
print("Count:", __length)
print("Min:", __min)
print("Max:", __max)
print("Mean:", __mean)
print("Median:", __median)
