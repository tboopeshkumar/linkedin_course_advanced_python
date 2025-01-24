# Manipulating string 

test_string = "The quick, brown fox jumped over the lazy dog."

# upper, lower, title
print(test_string.upper())
print(test_string.lower())
print(test_string.title())

# strip, lstrip, rstrip

test__str2 = "    This string has white space at the beginning and end.    "

print(test__str2.strip())
print(test__str2.lstrip())
print(test__str2.rstrip())

# split creates a sequence from a single string

words = test_string.split()
print(words)

words_comma = test_string.split(",")
print(words_comma)

# join concatenates a sequence of strings
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog."]
print(" ".join(words))