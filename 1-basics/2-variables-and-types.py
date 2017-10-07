
# Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare
# their type. Every variable in Python is an object.

# Numbers

# Integers
x = 1
print(x)

# Floats
y = 2.0
print(y)

z = float(3)
print(z)

# Strings
name1 = 'John Doe'
print(name1)

name2 = "Jane doe's cat"
print(name2)

a, b = 3, 4
print(a)
print(b)

# Lists
numbers = [1, 2, 3]
print(numbers)
print(numbers[0])
print(numbers[2])

strings = ['a', 'b', 'c']
print(strings)

mixed = [1, 'b', 3, 'd']
print(mixed)

# Tuples
info = ('John Doe', 25, 'Male', 'Software Engineer')
print(info)
print(info[0])

# Sets
colors = set(['red', 'green', 'blue', 'orange', 'yellow', 'purple'])
print(colors)

# Maps/Dictionaries
days = { 'MON': 'Monday', 'TUE': 'Tuesday', 'WED': 'Wednesday' }
print(days['TUE'])

days['THU'] = 'Thursday'
print(days)

nothing = None
print(nothing)