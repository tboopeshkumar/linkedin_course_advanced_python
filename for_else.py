# The for-else loop construct

# cehck if a number is prime

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break;
    else:
        print(num, "is prime")

is_prime(31)
is_prime(10)