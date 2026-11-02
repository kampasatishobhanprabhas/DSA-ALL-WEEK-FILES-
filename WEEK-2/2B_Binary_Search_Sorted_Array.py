# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

# week-2(2B).py - C/Users/shobh/AppData/Local/Programs/Python/Python3 14/week-2(28) py (3.14.7)
def binary search(arr, key, low, high):
if low > high:
return -1
mid = (low + high) // 2
if arr[mid] == key:
return mid
elif key < arr[mid]:
return binary_search(arr, key, low, mid - 1)
else:
return binary _search(arr, key, mid + 1, high)
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
x = int(input("Enter element: "))
arr.append (x)
arr.sort ()
