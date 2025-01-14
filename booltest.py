## Following evaluate to False

    # False and None evauate to false
    # Numeric zero values : 0, 0.0,  0j
    # Decimal(0), Fraction (0,x)
    # Empty sequences / collections: "", (), [], {}
    # Empty sets and ranges: set(), range(0)
    # Custom classes that override __bool__ and return False or return 0 from an overridden __len__ function 
        # class myClass:
        #     def __bool__(self):
        #         return False
        #     def __len__(self):
        #         return 0
                    
x = []

print(bool(x))

y = {}

print(bool(y))
