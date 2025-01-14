# Understanding Python scope

# decalar a variable in the global scope
x = 1

# define a local function with a variable "x"
def test():
    global x # This tells the function to use the global x
    x=15
    print(x)

#Run the test function and observe the two results.
test()
print(x)

x = x+5
print(x)
test()

# Nested functions create innter scopes. These are called closures:

def multipier_maker(factor):
    def multiplier(number):
        return number * factor
    return multiplier

doubler = multipier_maker(2)
tripler = multipier_maker(3)

print(doubler(7))
print(tripler(9))