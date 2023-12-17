student = {
    'id': '123456789',
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 21,
}

# Access dictionary values
print('*** Access dictionary values ***')
print('id: ', student['id'])
print('first: ', student['first_name'])
print('last: ', student['last_name'])
print('age: ', student['age'])

# Access dictionary values using get()
print('\n*** Access dictionary values using get() ***')
print('id: ', student.get('id'))
print('first: ', student.get('first_name'))
print('last: ', student.get('last_name'))
print('age: ', student.get('age'))

# Access dictionary values using get() with default value
print('\n*** Access dictionary values using get() with default value ***')
print('id: ', student.get('id', 'N/A'))
print('first: ', student.get('first_name', 'N/A'))
print('last: ', student.get('last_name', 'N/A'))
print('age: ', student.get('age', 'N/A'))

# Iterate over dictionary keys
print('\n*** Iterate over dictionary keys ***')
for key in student:
    print(key)

# Iterate over dictionary values
print('\n*** Iterate over dictionary values ***')
for key in student:
    print(student[key])

# Iterate over dictionary values using values()
print('\n*** Iterate over dictionary values using values() ***')
for value in student.values():
    print(value)

# Iterate over dictionary keys and values using items()
print('\n*** Iterate over dictionary keys and values using items() ***')
for key, value in student.items():
    print(key + ":", value)

# Add new key-value pair to dictionary
print('\n*** Add new key-value pair to dictionary ***')
student['email'] = 'john.d@uoregon.edu'
print(student)

# Update value for existing key
print('\n*** Update value for existing key ***')
student['email'] = 'john.doe@uoregon.edu'

# Delete key-value pair from dictionary
print('\n*** Delete key-value pair from dictionary ***')
del student['email']
print(student)

# Add a list to a dictionary
print('\n*** Add a list to a dictionary ***')
student['scores'] = [90, 80, 70, 60, 50]
print(student)

# Print list of scores
print('\n*** Print list of scores ***')
for score in student['scores']:
    print(score)

# Delete dictionary
print('\n*** Delete dictionary ***')
del student
