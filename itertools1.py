import itertools
# Iterools: count, cycle, accumulate

names = ['Cecilia', 'Lise', 'Marie']

# cycle iterate over a sequence repeatedly
cycler = itertools.cycle(names)

print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

# use count to create a simple counter

counter = itertools.count(start=100, step=10)
print(next(counter))
print(next(counter))

# accumulate creates an iterator that accumulates values

vals = [10, 20, 30, 40, 50, 40, 30]
acc = itertools.accumulate(vals, max)

print(list(acc))

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325]
update = lambda bal, pmt: round(bal * 1.04) - pmt
balances = itertools.accumulate(payments, update, initial=2000)
print(list(balances))