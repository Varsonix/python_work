    # Ok, given n, find it's absolute difference between n and 21
    # Example: n = 10
    # Solution: diff_21(10) returns 11
    # Example 2: diff_21(-10) returns 31

def diff_21(n):
    # I know there is probably an abs() function of some sort.
    # But I want to avoid imports first and see if I can do it via logic.
    # Run our logic first

    # Deciding to try to save a variable first (21 - n for Diff) was the
    # Culprit of the issue at first.
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

print(diff_21(10))
print(diff_21(-10))
print(diff_21(21))
# 2 is correct because 21-22 = -1 * -2 = 2 which is DOUBLE the ABSDIFF of 1
print(diff_21(22))
print(diff_21(31)) # 21-31 = -10 * -2 = 20 which is double 10 the ABSDIFF
print(diff_21(251))