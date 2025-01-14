# Example file for the Advaced Python Development workshop
# Using special names in Python

import collections
# __name__ is a special namme of the module
print("Module name:", __name__)

# __file__ contains the path to the file from which the module was loaded
print("File Path:", __file__)

# __package__ indicates the package that the module belongs to. 
print("Package:", __package__)
print(collections.__package__)

if __name__ == '__main__':
    print("This is the main module")