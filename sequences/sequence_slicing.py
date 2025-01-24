
# Sequences and slicing 

from collections import deque

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi']

print(names[1:4])
print(names[:3])
print(names[3:])

# reverse the list with step of -1
print(names[::-1])


# assigning sequeuesn

newnames = ['Andy', 'Stanley', 'Angela']

names[2:5] = newnames

print(names)

deque_names = deque(names)

for name in deque_names:
    print(name, ' ', end='')

