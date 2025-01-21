

sample_text = "The quick brown fox jumped over the lazy dog."
tempstr = sample_text.lower()

# Using find to find the first occurrence of a substring

print("First occurrance of 'The':", sample_text.find("The"))

# Using index to find the first occurrence of a substring(raises ValueError if not found)
print("First occurrance of 'fox':", sample_text.index("fox"))

try:
    print("First occurrance of 'fax':", sample_text.index("fax"))
except ValueError as e:
    print("ValueError:", e)

# The 'in' operator can be used to check if a substring is present in a string
print("Is 'fox' in the string?", "fox" in sample_text)


# Using rfind to find the last occurrence of a substring
print("Lat occurance of 'the':", sample_text.rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurance of 'The':", sample_text.rindex("The"))

# The replace() function will find content in the string and replace it
result = sample_text.replace("fox", "wolf")
print(result)