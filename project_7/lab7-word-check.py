# CS 122 fall 2023 lab 7
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description:

while True:
    if not (word := input("Enter search word: ").strip()):
        break
    fin = open("words_alpha.txt")
    count = 0
    word_found = False
    for line in fin:
        count += 1
        if word.lower() == line.strip().lower():
            word_found = True
            break
    fin.close()
    if word_found:
        print(f"Word {word} found")
    else:
        print(f"Word {word} not found")
