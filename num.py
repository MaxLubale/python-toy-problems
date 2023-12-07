def two_positive_numbers(a, b, c):
    # Count the number of positive numbers
    positive_counts = 0
    if a > 0:
        positive_counts += 1
    if b > 0:
        positive_counts += 1
    if c > 0:
        positive_counts += 1

    # Check if exactly two numbers are positive
    return positive_counts == 2


print(two_positive_numbers(2, 4, -3))   
 