# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

1D. AIM. Ina logistics company , the no . of possible ways to arrange in different parcels is
calculated using the factorial formula (n!). Develop a recursive program to calculate the
factorial of a given number.
def factorial (n):

if n == 0 orn ==1:

return 1

return n * factorial(n - 1)
n = int(input("Enter a number: "))
print ("Factorial =", factorial(n))
Outnut:
