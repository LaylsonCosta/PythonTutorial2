"""
Usage examples of strings methos
"""


# Replace Method
a = "1abc2abc3abc4abc"
print(a)
print(a.replace('abc', 'ABC', 2))

# Sub-Strings
# Starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
# 3rd parameter sets the amount of characters jumps
step = a[1:6:3]
print("**************")
print(sub)
print(step)

# write reverse
print(a[::-1])