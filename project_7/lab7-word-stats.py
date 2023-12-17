# CS 122 fall 2023 lab 7
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description:
count = 0
palindromes = 0
shortest_word = ""
longest_word = ""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic_letters = {}
for letter in letters:
    dic_letters.setdefault(letter, 0)
dic_letters.setdefault("Other", 0)
fin = open("words_alpha.txt")
for line in fin:
    count += 1
    line = line.strip()

    if line == line[::-1]:
        palindromes += 1

    if not shortest_word:
        shortest_word = line
    elif len(shortest_word) > len(line):
        shortest_word = line

    if not longest_word:
        longest_word = line
    elif len(longest_word) < len(line):
        longest_word = line

    if line[0].upper() in letters:
        dic_letters[line[0].upper()] += 1
    else:
        dic_letters['Other'] += 1

fin.close()
print(f"Count: {count}")
print(f"Longest word is {longest_word} ({len(longest_word)})")
print(f"Shortest word is {shortest_word} ({len(shortest_word)})")
print(f"Palindromes: {palindromes} ({round(palindromes / count * 100, 2)}%)")
print("First letter counts")
for key, value in dic_letters.items():
    print(f"{key}: {value} ({round(value / count * 100, 2)}%)")
