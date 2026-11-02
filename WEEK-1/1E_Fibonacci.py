# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

def fibonacci (n) :
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci (n - 1) + fibonacci (n - 2)
n = int (input ("Enter the number of terms: "))
print ("Fibonacci Series:")
for i in range (n):
print (fibonacci (i), end=" ")
>>
Fibonacci Series:
0112358 13 21 34
>>|
Explanation
