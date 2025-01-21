import string
import secrets

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)

# Define a test string 
testStr = "The quick brown fox jumped over the lazy dog."

# use an iterator to see if a string contains any punctuation
result = (c in string.punctuation for c in testStr)
print(*result)
if any(c in string.punctuation for c in testStr):
    print("The string contains punctuation")
else:
    print("The string does not contain punctuation")


# Generate a random password
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))

print(password)


# Check the strength of a password

def check_password_strengh(testPass):
    if (len(testStr) >= 10 and 
        any(char in string.punctuation for char in testPass) and
        any(char in string.ascii_lowercase for char in testPass) and
        any(char in string.ascii_uppercase for char in testPass) and
        any(char in string.digits for char in testPass)):

        return f"{testPass} is a strong password"
    else:
        return f"{testPass} is a weak password"

print(check_password_strengh("test"))
print(check_password_strengh("test123"))
print(check_password_strengh("Test123!"))
