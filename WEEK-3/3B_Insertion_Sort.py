# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

def insertion_sort (arr):
for i in range(1, len(arr)):
key = arr[i]
jzi-1
while j >= 0 and arr[j] > key:
arr(j + 1) = arr[j]
jej-1
arr[j + 1] = key
return arr
n = int(input ("Enter number of elements: "))
arr = [)
for i in range(n):
arr.append(int (input ("Enter element: ")))
result = insertion_sort (arr)
print ("Sorted array:", result)|
