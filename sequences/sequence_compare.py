import itertools

seq1 = [1,2,3,6,10,15,34,56]
seq2 = [1,2,5,7,9,18,22,38,91]

seq3 = (1,2,3,6,10,15,34,56)



print(seq1 == seq2)
print(seq1 > seq2)
print(seq1 < seq2)

# sequence have equl values but different number of items
seq4 = [10,20,30]
seq5 = [10,20,30, 40, 50]

print(seq5 > seq4)

# Sequence must be of the same type to compare
print(seq1 == seq3)
print(tuple(seq1) == seq3)

# use the all() function to compare sequences
result = all(x == y for x, y in itertools.zip_longest(seq1, seq3))
print(result)