import string

the_str = "This, is a test string!, can you find the punctuation!"

result = tuple({v for v in the_str if v in string.punctuation})

print(result)