# CS 122 fall 2023 lab 9
# Author: Bardia Ahmadi Dafchahi
# Credits: python := documentation
# Description:
def student():
    d = {}
    if idn := input('Enter student ID (or '' to quit): ').strip():
        d['id'] = idn
        d['last_name'] = input("Enter last name: ")
        d['first_name'] = input("Enter first name: ")
        if (age := input("Enter age: ")).isdigit():
            d['age'] = int(age)
        else:
            d['age'] = 0

    return d


students = []
while _student := student():
    students.append(_student)
print("List of Students:")
for student in students:
    print(student)
