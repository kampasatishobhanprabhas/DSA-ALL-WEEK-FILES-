# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

a I,
Probing, and Quadratic Probing.
# Hashing using Separate Chaining, Linear Probing, and Quadratic Probing
# Separate Chaining
def separate_chaining(keys, size):
table = [[] for _ in range(size)]
for key in keys:
index = key % size
table [index] .append (key)
print ("\nSeparate Chaining:")
for i in range(size):
print (i, ":", table(i])
# Linear Probing
def linear_probing(keys, size):
table = [None] * size
