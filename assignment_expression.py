import pprint

# regular assignment statemens assign a value

x = 5


# the assignment operator is part of an expression (walrun operator)

(xa := 10)

# without assignment operator

thestr1 = input("Value ? ")
while thestr1 != "exit":
    print(thestr1)
    thestr1 = input("Value? ")

# with assignment operator

while (thestr := input("Value ?")) != "exit":
    print(thestr)


# without assignment operator

values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]

l = len(values)
s = sum(values)

val_data = {
    "length": l,
    "total": s,
    "avg" : s / l
}


# with assignment operator : inline variables len, tot with local scope

val_data_1 = {
    "length": (len := len(values)),
    "total": (tot := sum(values)),
    "avg" : tot / len
}