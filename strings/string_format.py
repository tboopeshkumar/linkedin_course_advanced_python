
# Basic string formatting - center,ljust,rjust

width = 40

print("center".center(width, "-"))
print("left".ljust(width, "-"))
print("right".rjust(width, "-"))


val1 = 1234.5678
val2 = 109887.65
val3 = 12.99
val4 = -280.7

print(f"{val1}")
print(f"{val2}")
print(f"{val3}")
print(f"{val4}")


# Specify a precision and type
print(f"{val1:.2f}")
print(f"{val2:.2f}")
print(f"{val3:.2f}")
print(f"{val4:.2f}")

# Use alignment and width and leading zeros

print(f"{val1:<10.2f}")
print(f"{val1:>10.2f}")
print(f"{val1:^10.2f}")

print(f"{val1:<010.2f}")
print(f"{val1:>010.2f}")
print(f"{val1:^010.2f}")

# Use a grouping option and +/- signs
print(f"{val1:<-010.2f}")
print(f"{val4:>-010.2f}")
print(f"{val1:^+010.2f}")

# Create format specifiers dynamically
width = 10
precision = 2
format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)


format_spec = "{val:{width}.{precision}f}".format(val=val2, width=10, precision=2)
print(format_spec)

