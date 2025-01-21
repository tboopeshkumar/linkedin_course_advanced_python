import itertools

# product() produces the cartesiann product of input iterables  

cards = "A23456789TJQK"
suits = "SCHD"

deck = list(itertools.product(cards, suits))
print(len(deck), "cards")
print(deck)

# permutations() creates tuples of a given length with no repeated elements
teams = ("A", "B", "C", "D")
result = itertools.permutations(teams, 2)
print(list(result))


# combinations() creates tuples of a given length with no repeated elements
result = itertools.combinations(teams, 3)
print(list(result))

# combinations_with_replacement() creates tuples of a given length with repeated elements
result = itertools.combinations_with_replacement(teams, 3)
print(list(result))


input = [[2, 5, 20], [30,56], [8,4,28,31]]

# chain() combines several iterables into one long iterable

flatResult = itertools.chain(*input)

result = max(flatResult)

print(result)
