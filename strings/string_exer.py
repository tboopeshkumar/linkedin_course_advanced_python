import string
import itertools

def process_string(the_str, term):
    return {
        "Punctuation": sum(1 for c in the_str if c in string.punctuation),
        "Whitespace": sum(map(str.isspace, the_str)),
        "Lowercase": sum(map(str.islower, the_str)),
        "Uppercase": sum(map(str.isupper, the_str)),
        "Found": the_str.lower().find(term.lower()) >= 0,
        "Index": the_str.lower().find(term.lower()),
    }

def process_string_2(the_str, term):
    result =  {
        "Punctuation": 0,
        "Whitespace": 0,
        "Lowercase": 0,
        "Uppercase": 0,
        "Found": False,
        "Index": 0
    }

    for c in the_str:
        if c in string.punctuation:
            result["Punctuation"] += 1
        if c in string.whitespace:
            result["Whitespace"] += 1
        if c in string.ascii_lowercase:
            result["Lowercase"] += 1
        if c in string.ascii_uppercase:
            result["Uppercase"] += 1
    
    result["Found"] = term.lower() in the_str.lower()
    result["Index"] = the_str.lower().find(term.lower())

    return result

def main():
    test_string = "This, is a test string!"
    print(process_string_2(test_string, "Tdfadsest"))


if __name__ == '__main__':
    main()