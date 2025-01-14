import itertools

# Working with basic iterators in Python

# define a list of days in English and French
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_fr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']


for d in range(len(days)):
    print(d+1, days[d])

# the enumerate function

for i, d in enumerate(days):
    print(i, d)

# use zip to combine sequences
for m in zip(days, days_fr):
    print(m)

# use enumerate and zip together

for i, d in enumerate(zip(days, days_fr), start=1):
    print(i, d[0], "=", d[1], "in French")

# use zip_longest to combine sequences of different lengths

seq1 = ['one', 'two', 'three', 'four', 'five']
seq2 = ['1', '2', '3','4']
seq3 = "xyz"

result = itertools.zip_longest(seq1, seq2, seq3, fillvalue='-')

for r in result:
    print(r)
