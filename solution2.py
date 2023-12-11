def two_positive(a, b, c):
    positive_count = 0
    # updating the count
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    # result
    return positive_count == 2

# results
print(two_positive(1, 4, -7))    # Output will be True
print(two_positive(-9, 1, 9))    # Output will be True
print(two_positive(2, -10, 9))   # Output will be True
print(two_positive(-3, 5, 0))    # Output will be False
print(two_positive(8, 21, 10))   # Output will be False
print(two_positive(-21, -14, -7))# Output will be False
