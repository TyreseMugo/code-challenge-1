# PYTHON CODE CHALLENGE 1
# Description
This project includes three Python functions that perform different tasks:

convert_to_24hrs: This function takes an hour, minute, and period (am/pm) as input and converts it to a 24-hour format. It then returns the formatted time as a string.

# Examples
print(convert_to_24hrs(10, 50, "am"))  # Output will be 1050
print(convert_to_24hrs(10, 50, "pm"))  # Output will be 2250
print(convert_to_24hrs(12, 45, "am"))  # Output will be 0045
print(convert_to_24hrs(12, 45, "pm"))  # Output will be 1245
print(convert_to_24hrs(1, 20, "am"))   # Output will be 0120
print(convert_to_24hrs(1, 20, "pm"))   # Output will be 1320


two_positive: This function takes three numbers as input and returns True if exactly two of them are positive, and False otherwise.

# Examples
print(two_positive(1, 4, -7))    # Output will be True
print(two_positive(-9, 1, 9))    # Output will be True
print(two_positive(2, -10, 9))   # Output will be True
print(two_positive(-3, 5, 0))    # Output will be False
print(two_positive(8, 21, 10))   # Output will be False
print(two_positive(-21, -14, -7))# Output will be False


solve: This function takes a string as input, extracts consonant substrings, calculates their values, and returns the maximum value.
# Examples
print(solve("hello"))        # Output will be 52
print(solve("programming"))  # Output will be 111
print(solve("python"))       # Output will be 104