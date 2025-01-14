# Working with basic iterators in Python

# define a list of days in English and French
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_fr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

# user regular iteration over the days
for m in days:
    print(m)

# use iter() to create an iterator over a collection
# the next() function retrieves the next item from the iterator

days_iter = iter(days)
print(next(days_iter))
print(next(days_iter))
print(next(days_iter))

#iterate usinga function and a sentinel
with open('testfile.txt', 'r') as fp:
    for line in iter(f.readline, ''):
        print(line, end='')