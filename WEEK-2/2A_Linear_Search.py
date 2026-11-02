# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

a —

A week-2(2A) py -C/Users/shobhy/AppData/Local/Programs/Python/Python3 14/week-2(2A).py (3.14.7)
def linear_search(arr, key, index):

if index == len(arr):

return -1
if arr[index] == key:
return index

return linear_search(arr, key, index + 1)
n = int(input ("Enter number of elements: "))
arr = []
for i in range(n):

x = int (input ("Enter element: "))

arr.append (x)
key = int(input("Enter element to search: "))
result = linear_search(arr, key, 0)
if result == -1:

print ("Element not found")
else:

print ("Element found at index", result)
|
